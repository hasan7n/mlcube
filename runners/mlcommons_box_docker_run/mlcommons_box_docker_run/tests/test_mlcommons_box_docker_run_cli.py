from click.testing import CliRunner
from mlcommons_box_docker_run.__main__ import cli


runner = CliRunner()


def test_mlcommons_box_docker_run():
    response = runner.invoke(cli)
    assert response.exit_code == 0
    assert 'Usage: mlcommons_box_docker_run [OPTIONS] COMMAND [ARGS]...' in response.output
    assert '  configure  Configure docker environment for MLCommons-Box ML workload.' in response.output
    assert '  run        Run MLCommons-Box ML workload in the docker environment.' in response.output
