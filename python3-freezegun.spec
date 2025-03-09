#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	FreezeGun: Let your Python 2 tests travel through time
Summary(pl.UTF-8):	FreezeGun - umożliwienie testom Pythona 2 podróżowania w czasie
Name:		python3-freezegun
Version:	1.2.2
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/freezegun/
Source0:	https://files.pythonhosted.org/packages/source/f/freezegun/freezegun-%{version}.tar.gz
# Source0-md5:	40e783f950f4e17e1e0118dd6385b449
# https://patch-diff.githubusercontent.com/raw/spulec/freezegun/pull/397.patch
Patch0:		freezegun-pull397.patch
URL:		https://pypi.org/project/freezegun/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-dateutil >= 2.7
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreezeGun is a library that allows your Python tests to travel through
time by mocking the datetime module.

%description -l pl.UTF-8
FreezeGun to biblioteka pozwalająca testom w Pythonie podróżowanie w
czasie dzięki atrapie modułu datetime.

%prep
%setup -q -n freezegun-%{version}
%patch -P 0 -p1

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.rst CHANGELOG README.rst
%{py3_sitescriptdir}/freezegun
%{py3_sitescriptdir}/freezegun-%{version}-py*.egg-info
