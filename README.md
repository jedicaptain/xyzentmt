# xyzentmt

run = "python app.py"
language = "python3"
hidden = ["venv", ".config","**/__pycache__","**/.mypy_cache", "**/*.pyc"]

[nix]
channel = "stable-22_11"

[env]
VIRTUAL_ENV = "/home/runner/${REPL_SLUG}/venv"
PATH = "${VIRTUAL_ENV}/bin"
PYTHONPATH = "$PYTHONHOME/lib/python3.10:${VIRTUAL_ENV}/lib/python3.10/site-packages"
REPLIT_POETRY_PYPI_REPOSITORY = "https://package-proxy.replit.com/pypi/"
MPLBACKEND = "TkAgg"
POETRY_CACHE_DIR = "${HOME}/${REPL_SLUG}/.cache/pypoetry"

[unitTest]
  language = "python3"
  support = true

[debugger.interactive]
  transport = "localhost:0"
  startCommand = ["dap-python", "main.py"]

[debugger.interactive.integratedAdapter]
    dapTcpAddress = "localhost:0"

  [debugger.interactive.initializeMessage]
    command = "initialize"
    type = "request"

[debugger.interactive.initializeMessage.arguments]
      adapterID = "debugpy"
      clientID = "replit"
      clientName = "replit.com"
      columnsStartAt1 = true
      linesStartAt1 = true
      locale = "en-us"
      pathFormat = "path"
      supportsInvalidatedEvent = true
      supportsProgressReporting = true
      supportsRunInTerminalRequest = true
      supportsVariablePaging = true
      supportsVariableType = true

    
    [debugger.interactive.launchMessage]
    command = "attach"
    type = "request"

      [debugger.interactive.launchMessage.arguments]
      logging = {}

# Configures the packager.
[packager]
language = "python3"
ignoredPackages = ["unit_tests"]

  [packager.features]
  enabledForHosting = false
  # Enable searching packages from the sidebar.
  packageSearch = true
  # Enable guessing what packages are needed from the code.
  guessImports = true

# These are the files that need to be preserved when this 
# language template is used as the base language template
# for Python repos imported from GitHub
[gitHubImport]
requiredFiles = [".replit", "replit.nix", ".config", "venv"]

[languages]

[languages.python3]
pattern = "**/*.py"

[languages.python3.languageServer]
start = "pylsp"
