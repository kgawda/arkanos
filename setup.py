from setuptools import setup, find_packages, Extension

setup(
    name="arkanos",
    packages=find_packages(),
    ext_modules=[
        Extension(
            'greet',
            sources=['arkanos/c_extension/greetmodule.c'],
            py_limited_api=True
        )
    ]
)
