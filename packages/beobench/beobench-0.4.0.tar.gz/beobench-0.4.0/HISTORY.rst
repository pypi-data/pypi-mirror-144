=======
History
=======

0.4.0 (2022-03-28)
------------------

* Make dependencies that are only used inside experiment/gym containers optional (for all dependencies install via ``pip install beobench[extended]``)
* Add two part experiment image build process so that there is shared beobench installation dockerfile
* Add support for yaml config files (!)
* Overhaul of documentation, including new envs page and new theme
* Enable RLlib free experiment containers when not required
* Add beobench_contrib as submodule
* Simplify Pypi readme file
* Remove GPU requirement for devcontainer

0.3.0 (2022-02-14)
------------------

* Add complete redesign of CLI: main command changed from ``python -m beobench.experiment.scheduler`` to ``beobench run``.
* Add support for energym environments
* Add support for MLflow experiment tracking
* Add support for custom agents


0.2.1 (2022-02-03)
------------------

* Add integration with sinergym
* Move gym integrations to separate beobench_contrib repo
* Make usage of GPUs in containers optional

0.2.0 (2022-01-18)
------------------

* Enable adding custom environments to beobench with *docker build context*-based syntax
* Save experiment results on host machine
* Major improvements to documentation
* Remove unnecessary wandb arguments in main CLI

0.1.0 (2022-01-10)
------------------

* First release on PyPI.
