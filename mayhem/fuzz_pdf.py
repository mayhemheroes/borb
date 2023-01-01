#!/usr/bin/env python3

import atheris
import sys
import fuzz_helpers

with atheris.instrument_imports(include=['borb']):
    from borb.pdf import PDF


def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        with fdp.ConsumeMemoryFile(as_bytes=True, all_data=True) as f:
            file = PDF.loads(f)
        PDF.dumps(file)
    except AssertionError:
        return -1

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
