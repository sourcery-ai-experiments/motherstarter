"""
motherstarter noxfile
"""

# Import modules
import nox


@nox.session(python=["3.10", "3.11"])
def lint(session):
    """
    Run all linting tests.
    Nox run black, pylama, yamllint and bandit

    Args:
        session: nox session

    Returns:
        N/A

    Raises:
        N/A
    """
    session.install("-r", "requirements.txt")
    session.run("ruff", "format", ".", "--check")
    session.run("ruff", "check", ".")
    session.run("yamllint", ".")
    session.run(
        "bandit", "motherstarter/", "--configfile", "pyproject.toml", "--recursive", "--format", "json", "--verbose"
    )
    session.run("python", "-m", "mypy", "--config-file", "pyproject.toml")


@nox.session(python=["3.10", "3.11"])
def ruff_format(session):
    """
    Nox run ruff format

    Args:
        session: nox session

    Returns:
        N/A

    Raises:
        N/A

    """
    session.install("-r", "requirements.txt")
    session.run("ruff", "format", ".", "--check")


@nox.session(python=["3.10", "3.11"])
def ruff_check(session):
    """
    Nox run ruff check

    Args:
        session: nox session

    Returns:
        N/A

    Raises:
        N/A

    """
    session.install("-r", "requirements.txt")
    session.run("ruff", "check", ".")


@nox.session(python=["3.10", "3.11"])
def yamllint(session):
    """
    Nox run yamllint

    Args:
        session: nox session

    Returns:
        N/A

    Raises:
        N/A

    """
    session.install("-r", "requirements.txt")
    session.run("yamllint", ".")


@nox.session(python=["3.10", "3.11"])
def bandit(session):
    """
    Nox run bandit

    Args:
        session: nox session

    Returns:
        N/A

    Raises:
        N/A

    """
    session.install("-r", "requirements.txt")
    session.run(
        "bandit", "motherstarter/", "--configfile", "pyproject.toml", "--recursive", "--format", "json", "--verbose"
    )


@nox.session(python=["3.10", "3.11"])
def mypy(session):
    """
    Nox run mypy

    Args:
        session: nox session

    Returns:
        None

    Raises:
        N/A
    """
    session.install("-r", "requirements.txt")
    session.run("python", "-m", "mypy", "--config-file", "pyproject.toml")


@nox.session(python=["3.10", "3.11"])
def tests(session):
    """
    Nox run tests using pytest

    Args:
        session: nox session

    Returns:
        N/A

    Raises:
        N/A

    """
    session.install("-r", "requirements.txt")
    session.run("pytest", "--cov=./", "--cov-report=xml")
