import nox

nox.options.reuse_existing_virtualenvs = True


@nox.session(reuse_venv=True)
def lint(session):
	session.install('-U', '.[lint]')
	session.run('flake8', 'src/')
