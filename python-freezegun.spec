#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	FreezeGun: Let your Python 2 tests travel through time
Summary(pl.UTF-8):	FreezeGun - umożliwienie testom Pythona 2 podróżowania w czasie
Name:		python-freezegun
Version:	0.3.12
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/freezegun/
Source0:	https://files.pythonhosted.org/packages/source/f/freezegun/freezegun-%{version}.tar.gz
# Source0-md5:	7a289a0473100e726335ea26fb0ef8de
Patch0:		%{name}-mock.patch
URL:		https://pypi.org/project/freezegun/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-dateutil >= 2.1
BuildRequires:	python-mock
BuildRequires:	python-modules-sqlite
BuildRequires:	python-pytest
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-dateutil >= 2.1
BuildRequires:	python3-pytest
BuildRequires:	python3-six
%endif
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreezeGun is a library that allows your Python tests to travel through
time by mocking the datetime module.

%description -l pl.UTF-8
FreezeGun to biblioteka pozwalająca testom w Pythonie podróżowanie w
czasie dzięki atrapie modułu datetime.

%package -n python3-freezegun
Summary:	FreezeGun: Let your Python 3 tests travel through time
Summary(pl.UTF-8):	FreezeGun - umożliwienie testom Pythona 3 podróżowania w czasie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-freezegun
FreezeGun is a library that allows your Python tests to travel through
time by mocking the datetime module.

%description -n python3-freezegun -l pl.UTF-8
FreezeGun to biblioteka pozwalająca testom w Pythonie podróżowanie w
czasie dzięki atrapie modułu datetime.

%prep
%setup -q -n freezegun-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
# uuid tests fail with python3.8 (as of 0.3.12)
%{__python3} -m pytest --deselect tests/test_uuid.py::test_uuid1_future --deselect tests/test_uuid.py::test_uuid1_past tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.rst CHANGELOG README.rst
%{py_sitescriptdir}/freezegun
%{py_sitescriptdir}/freezegun-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-freezegun
%defattr(644,root,root,755)
%doc AUTHORS.rst CHANGELOG README.rst
%{py3_sitescriptdir}/freezegun
%{py3_sitescriptdir}/freezegun-%{version}-py*.egg-info
%endif
