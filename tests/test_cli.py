"""
Unit tests for Minimal Universal CLI (af / agy-factory)
"""

import pytest
from click.testing import CliRunner
from sdlc_factory.cli import main


def test_cli_universal_intent():
    runner = CliRunner()
    res = runner.invoke(main, ["Build payment gateway microservice"])
    assert res.exit_code == 0
    assert "Compiling Intent 'Build payment gateway microservice'" in res.output
    assert "Compilation Complete!" in res.output


def test_cli_universal_auto_onboard():
    runner = CliRunner()
    with runner.isolated_filesystem():
        # Create dummy file to simulate existing codebase
        with open("app.py", "w") as f:
            f.write("# dummy app")
        res = runner.invoke(main, [])
        assert res.exit_code == 0
        assert "Codebase detected -> Auto-Onboarding" in res.output
        assert "Codebase is 100% SDLC Factory Onboarded!" in res.output


def test_cli_universal_auto_init():
    runner = CliRunner()
    with runner.isolated_filesystem():
        # Empty directory -> Auto-Init
        res = runner.invoke(main, [])
        assert res.exit_code == 0
        assert "Empty directory detected -> Initiating New SDLC Factory Project" in res.output


def test_cli_universal_prove():
    runner = CliRunner()
    res = runner.invoke(main, ["--prove", "Loan"])
    assert res.exit_code == 0
    assert "Running Z3 SMT Solver Invariant Verification" in res.output
    assert "Z3 SMT Solver proved invariant safety" in res.output
