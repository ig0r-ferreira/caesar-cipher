from unittest import TestCase, mock

from typer.testing import CliRunner

from caesar_cipher.cli import __version__, app, on_stdout

runner = CliRunner()


class TestCLI(TestCase):
    def test_app_should_return_exit_code_equal_to_0(self) -> None:
        result = runner.invoke(app)
        self.assertEqual(result.exit_code, 0)

    def test_version_option_should_return_cli_name_and_version(self) -> None:
        result = runner.invoke(app, '--version')
        self.assertEqual(result.stdout, f'{app.info.name} {__version__}\n')

    @mock.patch('builtins.print')
    def test_on_stdout_decorator_should_return_function_result_on_stdout(
        self, mock_stdout
    ) -> None:
        def hello():
            return 'Caesar Cipher'

        on_stdout(hello)()
        mock_stdout.assert_called_with('Caesar Cipher')
