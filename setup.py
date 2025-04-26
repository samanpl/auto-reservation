from setuptools import setup, find_packages

setup(
    name="auto_reservation_ik",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "auto_reservation_ik=main:main",  # command=path.to.function
        ],
    },
)
