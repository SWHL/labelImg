#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from pathlib import Path
from sys import platform as _platform

from get_pypi_latest_version import GetPyPiLatestVersion
from setuptools import find_namespace_packages, setup

cur_dir = Path(__file__).resolve().parent

NAME = "labelImg2"
REQUIRED_DEP = ["pyqt5", "lxml"]


def get_readme() -> str:
    root_dir = Path(__file__).resolve().parent
    readme_path = str(root_dir / "docs" / "doc_whl.md")
    with open(readme_path, "r", encoding="utf-8") as f:
        readme = f.read()
    return readme


obtainer = GetPyPiLatestVersion()
try:
    latest_version = obtainer(NAME)
except ValueError:
    latest_version = "0.0.1"

VERSION_NUM = obtainer.version_add_one(latest_version)

SET_REQUIRES = []
if _platform == "linux" or _platform == "linux2":
    # linux
    print("linux")
elif _platform == "darwin":
    # MAC OS X
    SET_REQUIRES.append("py2app")

resources_dir = cur_dir / "labelImg" / "resources"
OPTIONS = {
    "argv_emulation": True,
    "iconfile": str(resources_dir / "icons" / "app.icns"),
}

# 优先提取commit message中的语义化版本号，如无，则自动加1
if len(sys.argv) > 2:
    match_str = " ".join(sys.argv[2:])
    matched_versions = obtainer.extract_version(match_str)
    if matched_versions:
        VERSION_NUM = matched_versions
sys.argv = sys.argv[:2]

setup(
    name=NAME,
    version=VERSION_NUM,
    description="LabelImg is a graphical image annotation tool and label object bounding boxes in images",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    author="SWHL",
    author_email="liekkaskono@163.com",
    url="https://github.com/SWHL/labelImg",
    python_requires=">=3.6,<3.12",
    package_data={"": ["*.txt", "*.png", "*.svg", "*.icns", "*.properties"]},
    package_dir={"": NAME},
    packages=find_namespace_packages(where=NAME),
    entry_points={"console_scripts": ["labelImg=labelImg2.main:main"]},
    include_package_data=True,
    install_requires=REQUIRED_DEP,
    license="MIT license",
    keywords="labelImg labelTool development annotation deeplearning",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    options={"py2app": OPTIONS},
    setup_requires=SET_REQUIRES,
)
