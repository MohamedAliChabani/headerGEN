import yaml
import gen
import sys

def write_config(config):
    with open(sys.argv[2], "w", encoding="utf-8") as header:
        gen.write_headers(header, config)
        gen.write_classes(header, config)

def main():
    if len(sys.argv) < 3:
        print(f"Usage: python3 {sys.argv[0]} <config.yml> <header.h>")
        return

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
        write_config(config)

if __name__ == "__main__":
    main()
