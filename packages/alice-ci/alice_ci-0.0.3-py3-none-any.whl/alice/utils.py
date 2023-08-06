import yaml

from alice.exceptions import ConfigException


class ConfigParser:
    def __init__(self, file_path, factory) -> None:
        with open(file_path) as f:
            self.config = yaml.safe_load(f)
        self.factory = factory
        if "runners" in self.config:
            if "global" in self.config["runners"]:
                self.factory.set_globals(self.__gen_globals())
            self.factory.update_runners(self.config["runners"])
        self.jobs = self.__get_jobs()

    # Initialize env, workdir if not present
    def __gen_globals(self):
        globals = self.config["runners"]["global"]
        if "env" not in globals:
            globals["env"] = []
        if "workdir" not in globals:
            globals["workdir"] = None
        return globals

    def __get_jobs(self):
        if "jobs" in self.config:
            jobs = {}
            for job_spec in self.config["jobs"]:
                name = job_spec["name"]
                if name in jobs:
                    raise ConfigException(f"Job with name {name} already exists!")

                jobs[name] = job_spec
            return jobs
        else:
            raise ConfigException("No jobs defined in config")

    def execute_job(self, job_name):
        if job_name in self.jobs:
            # Pass the job_spec to a runner
            runner = self.factory.get_runner(self.jobs[job_name]["type"])
            runner.run(self.jobs[job_name])
