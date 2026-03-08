from pathlib import Path
from setuptools import setup, find_packages

ROOT = Path(__file__).parent


def parse_requirements(filename="requirements.txt"):
    req_path = ROOT / filename
    requirements = []

    for line in req_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith(("-r ", "--requirement ")):
            continue
        if line.startswith(("-e ", "--editable ")):
            continue
        requirements.append(line)

    return requirements


def read_readme():
    readme_path = ROOT / "README.md"
    if readme_path.exists():
        return readme_path.read_text(encoding="utf-8")
    return ""


setup(
    name="keynet",
    version="0.1.0",
    description="Key.Net feature extraction package",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    author="Your Name",
    license="MIT",  # change if needed
    packages=find_packages(
        exclude=[
            "imgs",
            "plot",
            "extracted_features",
            "__pycache__",
        ]
    ),
    include_package_data=True,
    package_data={
        "keynet": [
            "model/weights/*.pth",
            "model/HyNet/weights/*.pth",
        ],
    },
    install_requires=parse_requirements(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "keynet-extract=keynet.extract_kpts_dsc:main",
        ],
    },
    zip_safe=False,
)
