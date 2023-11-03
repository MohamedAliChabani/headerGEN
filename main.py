import yaml
import gen

def write_config(config):
    with open("test.h", "w", encoding="utf-8") as header:
        gen.write_headers(header, config)
        gen.write_classes(header, config)

def main():
    with open("config.yml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
        write_config(config)

if __name__ == "__main__":
    main()
