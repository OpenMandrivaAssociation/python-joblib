%define module joblib

Name:		python-joblib
Summary:	Lightweight pipelining with Python functions
Version:	1.5.3
Release:	2
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/joblib/
Source0:	https://files.pythonhosted.org/packages/source/j/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# See https://github.com/joblib/joblib/pull/1775
Patch0:	1.5.3-unvendor-cloudpickle.patch

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	fdupes
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Recommends:	python%{pyver}dist(lz4)
Recommends:	python%{pyver}dist(numpy)
Recommends:	python%{pyver}dist(psutil)

%description
%{module} is a set of tools to provide lightweight pipelining in Python.
In particular:

* transparent disk-caching of functions and lazy re-evaluation
  (memoize pattern).
* easy simple parallel computing.

%{module} is optimized to be fast and robust on large data in particular
and has specific optimizations for numpy arrays.

%prep -a
# Remove bundled egg-info
rm -rf %{module}-egg.info
# To match with Patch0 PR
rm -rf joblib/externals/cloudpickle/

%install -a
%fdupes %{buildroot}%{python_sitelib}

%files
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
