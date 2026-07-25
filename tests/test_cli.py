"""
Unit tests for CLI commands (init, onboard, compile, prove)
"""

import pytest
from click.testing import CliRunner
from sdlc_factory.cli import main


def test_cli_init():
    runner = CliRunner()
    with runner.isolated_filesystem():
        res = runner.invoke(main, ["init", "--name", "PaymentGateway", "--prompt", "Build payment service"])
        assert res.exit_code == 0
        assert "Initiating Brand New SDLC Factory Project" in res.output
        assert "PaymentGateway" in res.output


def test_cli_onboard():
    runner = CliRunner()
    with runner.isolated_filesystem():
        res = runner.invoke(main, ["onboard"])
        assert res.exit_code == 0
        assert "Scanning existing codebase" in res.output
        assert "Codebase is 100% SDLC Factory Onboarded!" in res.output
