# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		module		fasteners
%define		egg_name	fasteners
%define		pypi_name	fasteners
Summary:	Provides useful locks
Name:		python-%{pypi_name}
# 0.16.2 - latest with python2 support
Version:	0.16.2
Release:	4
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://pypi.debian.net/fasteners/fasteners-%{version}.tar.gz
# Source0-md5:	dcc86737f47f7e8da4ec21f466fe90dd
URL:		https://pypi.python.org/pypi/fasteners
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-monotonic
BuildRequires:	python-testtools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides useful locks.

%package -n python3-%{module}
Summary:	Provides useful locks
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
Provides useful locks

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py_install
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
