from setuptools import setup

# This packaging is by Sweet. The rest of the repository is forked from Queue-It.

with open('README.md', 'r') as input:
    long_description = input.read()

setup(
    name='queueit_knownuser_v3',
    version="1.1.0",
    description='A Python implementation of Queue-It\'s KnownUser V3',
    long_description=long_description,
    keywords='queue sweet',
    license='Proprietary (© Sweet)',
    author="Owen Miller",
    include_package_data=True,
    author_email='Owen Miller <owen@sweet.io>',
    python_requires='>=3.7',
    url='https://github.com/sweet-io-org/KnownUser.V3.Python',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3 :: Only',
        "Operating System :: OS Independent",
    ],
    packages=['queueit_knownuserv3'],
    package_dir={'queueit_knownuserv3': '.'},  # Map package name to root directory
    py_modules=['connector_diagnostics', 'http_context_providers', 'integration_config_helpers', 'known_user', 'models',
                'queue_url_params', 'queueit_helpers', 'user_in_queue_service',
                'user_in_queue_state_cookie_repository', 'token_generation'],
    install_requires=[]
)
