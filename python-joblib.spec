Summary:	Lightweight pipelining with Python functions
Name:		python-joblib
Version:	1.3.2
Release:	1
License:	BSD 3-Clause
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/j/joblib/joblib-%{version}.tar.gz
URL:		https://pypi.org/project/joblib/
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Lightweight pipelining with Python functions

%files
%{py_sitedir}/joblib
%{py_sitedir}/joblib-*.*-info

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n joblib-%{version}

%build
%py_build

%install
%py_install

