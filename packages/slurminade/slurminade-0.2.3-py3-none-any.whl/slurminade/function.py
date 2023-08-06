import inspect
import os.path
import shlex
import shutil
import subprocess
import sys
import json
import simple_slurm
from .guard import guard_recursive_distribution
from .conf import _get_conf


class SlurmFunction:
    function_map = {}
    mainf = None

    def __init__(self, slurm_conf, func):
        conf = _get_conf(slurm_conf)
        self.slurm = simple_slurm.Slurm(**conf)
        self.fname = func.__name__
        self.func = func
        if func.__name__ in self.function_map:
            raise RuntimeError("Slurminade functions must have unique names!")
        self.function_map[func.__name__] = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def _serialize_args(self, *args, **kwargs):
        inspect.signature(self.func).bind(*args, **kwargs)
        data = {"args": args, "kwargs": kwargs}
        serialized = json.dumps(data)
        if len(serialized) > 300:
            print(f"WARNING: Using slurminde function {self.fname} with long function "
                  f"arguments ({len(serialized)}. This can be bad.")
        return serialized

    def _get_command_list(self, *args, **kwargs):
        import __main__
        mainf = __main__.__file__
        if not os.path.isfile(mainf) or not mainf.endswith(".py"):
            raise RuntimeError("Cannot reproduce function call from command line.")

        argd = self._serialize_args(*args, **kwargs)
        slurm_task = [sys.executable, "-m", "slurminade.execute", mainf, self.fname, argd]
        return slurm_task

    def _get_command_with_quotes(self, *args, **kwargs):
        cmd_list = self._get_command_list(*args, **kwargs)
        # Quote the json arguments because sbatch cannot take a list.
        cmd_s = " ".join(cmd_list[:-1])+f" {shlex.quote(cmd_list[-1])}"
        return cmd_s

    def distribute(self, *args, **kwargs):
        if shutil.which("sbatch"):
            self.force_distribute(*args, **kwargs)
        else:
            print("SBATCH is not available. Running code locally. "
                  "If you do not want this, use `force_distribute'.")
            self(*args, **kwargs)

    def force_distribute(self, *args, **kwargs):
        guard_recursive_distribution()
        slurm_task = self._get_command_with_quotes(*args, **kwargs)
        self.slurm.sbatch(" ".join(slurm_task))

    def local(self, *args, **kwargs):
        """
        This function simulates a distribution but runs on the local computer.
        Great for debugging.
        """
        slurm_task = self._get_command_list(*args, **kwargs)
        subprocess.run(slurm_task, shell=False, check=True)

    @staticmethod
    def call(func_id, argj):
        argd = json.loads(argj)
        SlurmFunction.function_map[func_id](*argd["args"], **argd["kwargs"])


def slurmify(f=None, **args):
    if f:  # use default parameters
        return SlurmFunction({}, f)
    else:
        def dec(func):
            return SlurmFunction(args, func)

        return dec


def srun(command, conf: dict = None, simple_slurm_kwargs: dict = None):
    """
    Just calling simple_slurm's srun but with default parameters of slurminade.
    `srun` executes the command on a slurm node but waits for the return.
    :param command: The command to be executed.
    :param conf: Slurm configuration changes just for this command.
    :param simple_slurm_kwargs: Use this to change the arguments passed to simple_slurm.
    :return: The return of `simple_slurm.srun`.
    """
    conf = _get_conf(conf)
    slurm = simple_slurm.Slurm(**conf)
    if simple_slurm_kwargs:
        return slurm.srun(command, **simple_slurm_kwargs)
    else:
        return slurm.srun(command)


def sbatch(command, conf: dict = None, simple_slurm_kwargs: dict = None):
    """
    Just calling simple_slurm's sbatch but with default parameters of slurminade.
    `sbatch` executes the command on a slurm node and returns directly.
    :param command: The command to be executed.
    :param conf: Slurm configuration changes just for this command.
    :param simple_slurm_kwargs: Use this to change the arguments passed to simple_slurm.
    :return: The return of `simple_slurm.sbatch`.
    """
    conf = _get_conf(conf)
    slurm = simple_slurm.Slurm(**conf)
    slurm.sbatch(command, )
    if simple_slurm_kwargs:
        return slurm.sbatch(command, **simple_slurm_kwargs)
    else:
        return slurm.sbatch(command)
