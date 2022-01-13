HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = "\033[1m"

def disable():
    HEADER = ''
    OKBLUE = ''
    OKGREEN = ''
    WARNING = ''
    FAIL = ''
    ENDC = ''

def ok(msg):
    print(OKGREEN + str(msg) + ENDC)

def info(msg):
    print(OKBLUE + str(msg) + ENDC)

def warn(msg):
    print(WARNING + str(msg) + ENDC)

def err(msg):
    print(FAIL + str(msg) + ENDC)
