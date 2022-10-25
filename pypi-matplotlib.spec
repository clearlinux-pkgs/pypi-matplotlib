#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x8D86E7FAE5EB0C10 (quantum.analyst@gmail.com)
#
Name     : pypi-matplotlib
Version  : 3.5.2
Release  : 103
URL      : https://files.pythonhosted.org/packages/2f/be/7d6e073a3eb740ebeba43a69f5de2b141fea50b801e24e0ae024ac94d4ac/matplotlib-3.5.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/2f/be/7d6e073a3eb740ebeba43a69f5de2b141fea50b801e24e0ae024ac94d4ac/matplotlib-3.5.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/2f/be/7d6e073a3eb740ebeba43a69f5de2b141fea50b801e24e0ae024ac94d4ac/matplotlib-3.5.2.tar.gz.asc
Summary  : Python plotting package
Group    : Development/Tools
License  : Apache-1.1 BSD-3-Clause CC-BY-4.0 CC0-1.0 HPND MIT OFL-1.0 OFL-1.1 Python-2.0
Requires: pypi-matplotlib-filemap = %{version}-%{release}
Requires: pypi-matplotlib-lib = %{version}-%{release}
Requires: pypi-matplotlib-license = %{version}-%{release}
Requires: pypi-matplotlib-python = %{version}-%{release}
Requires: pypi-matplotlib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : cairo-dev
BuildRequires : freetype-dev
BuildRequires : gtk+-dev
BuildRequires : gtk3-dev
BuildRequires : libpng-dev
BuildRequires : pypi(certifi)
BuildRequires : pypi(cycler)
BuildRequires : pypi(fonttools)
BuildRequires : pypi(kiwisolver)
BuildRequires : pypi(numpy)
BuildRequires : pypi(packaging)
BuildRequires : pypi(pillow)
BuildRequires : pypi(py)
BuildRequires : pypi(pyparsing)
BuildRequires : pypi(python_dateutil)
BuildRequires : pypi(pytz)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(setuptools_scm_git_archive)
BuildRequires : pypi(tornado)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
BuildRequires : python3-tcl
BuildRequires : qhull-dev

%description
|PyPi|_ |Downloads|_ |NUMFocus|_
|DiscourseBadge|_ |Gitter|_ |GitHubIssues|_ |GitTutorial|_

%package filemap
Summary: filemap components for the pypi-matplotlib package.
Group: Default

%description filemap
filemap components for the pypi-matplotlib package.


%package lib
Summary: lib components for the pypi-matplotlib package.
Group: Libraries
Requires: pypi-matplotlib-license = %{version}-%{release}
Requires: pypi-matplotlib-filemap = %{version}-%{release}

%description lib
lib components for the pypi-matplotlib package.


%package license
Summary: license components for the pypi-matplotlib package.
Group: Default

%description license
license components for the pypi-matplotlib package.


%package python
Summary: python components for the pypi-matplotlib package.
Group: Default
Requires: pypi-matplotlib-python3 = %{version}-%{release}

%description python
python components for the pypi-matplotlib package.


%package python3
Summary: python3 components for the pypi-matplotlib package.
Group: Default
Requires: pypi-matplotlib-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(matplotlib)
Requires: cycler
Requires: pypi(cycler)
Requires: pypi(fonttools)
Requires: pypi(kiwisolver)
Requires: pypi(numpy)
Requires: pypi(packaging)
Requires: pypi(pillow)
Requires: pypi(pyparsing)
Requires: pypi(python_dateutil)

%description python3
python3 components for the pypi-matplotlib package.


%prep
%setup -q -n matplotlib-3.5.2
cd %{_builddir}/matplotlib-3.5.2
pushd ..
cp -a matplotlib-3.5.2 buildavx2
popd

%build
## build_prepend content
sed -e 's|#system_freetype = False|system_freetype = True|' -e 's|#system_qhull = False|system_qhull = True|' mplsetup.cfg.template > mplsetup.cfg
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666723792
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
## build_prepend content
sed -e 's|#system_freetype = False|system_freetype = True|' -e 's|#system_qhull = False|system_qhull = True|' mplsetup.cfg.template > mplsetup.cfg
## build_prepend end
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-matplotlib
cp %{_builddir}/matplotlib-%{version}/LICENSE/LICENSE %{buildroot}/usr/share/package-licenses/pypi-matplotlib/3683efd59fb44e798efb22fd086a5b1e3a0aa700 || :
cp %{_builddir}/matplotlib-%{version}/LICENSE/LICENSE_AMSFONTS %{buildroot}/usr/share/package-licenses/pypi-matplotlib/91cf189e02755085234dd321326345846bf2949f || :
cp %{_builddir}/matplotlib-%{version}/LICENSE/LICENSE_BAKOMA %{buildroot}/usr/share/package-licenses/pypi-matplotlib/9fa4f855f33fa4ed73c9e6865d534a4f0f910610 || :
cp %{_builddir}/matplotlib-%{version}/LICENSE/LICENSE_COLORBREWER %{buildroot}/usr/share/package-licenses/pypi-matplotlib/47a57a5629a135f4301bf8181c5e244e1baf5759 || :
cp %{_builddir}/matplotlib-%{version}/LICENSE/LICENSE_JSXTOOLS_RESIZE_OBSERVER %{buildroot}/usr/share/package-licenses/pypi-matplotlib/920b5b7e7e79918ab41e714c4002f3ad4a8fdcfc || :
cp %{_builddir}/matplotlib-%{version}/LICENSE/LICENSE_QT4_EDITOR %{buildroot}/usr/share/package-licenses/pypi-matplotlib/04bb73e33817fa6c0c1259344f7326b408e12885 || :
cp %{_builddir}/matplotlib-%{version}/LICENSE/LICENSE_SOLARIZED %{buildroot}/usr/share/package-licenses/pypi-matplotlib/81b71443d2a101a27194d8d7e0494a93e557a824 || :
cp %{_builddir}/matplotlib-%{version}/LICENSE/LICENSE_YORICK %{buildroot}/usr/share/package-licenses/pypi-matplotlib/fd0bb2832315e88d7a06dd4f28a73f4eac46d3c6 || :
cp %{_builddir}/matplotlib-%{version}/doc/_static/fa/LICENSE %{buildroot}/usr/share/package-licenses/pypi-matplotlib/38f5fae1676b8f00409b0fb2979799ed35320999 || :
cp %{_builddir}/matplotlib-%{version}/doc/devel/license.rst %{buildroot}/usr/share/package-licenses/pypi-matplotlib/96cdc9c40477ab698d63b8c83fab29e2a8f72527 || :
cp %{_builddir}/matplotlib-%{version}/extern/agg24-svn/src/copying %{buildroot}/usr/share/package-licenses/pypi-matplotlib/467189783f672de8baca8b34e798fa2da64166a5 || :
cp %{_builddir}/matplotlib-%{version}/lib/matplotlib/mpl-data/fonts/ttf/LICENSE_DEJAVU %{buildroot}/usr/share/package-licenses/pypi-matplotlib/23e8fed3e3499427ef5a80cbff0aca0946140493 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-matplotlib

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-matplotlib/04bb73e33817fa6c0c1259344f7326b408e12885
/usr/share/package-licenses/pypi-matplotlib/23e8fed3e3499427ef5a80cbff0aca0946140493
/usr/share/package-licenses/pypi-matplotlib/3683efd59fb44e798efb22fd086a5b1e3a0aa700
/usr/share/package-licenses/pypi-matplotlib/38f5fae1676b8f00409b0fb2979799ed35320999
/usr/share/package-licenses/pypi-matplotlib/467189783f672de8baca8b34e798fa2da64166a5
/usr/share/package-licenses/pypi-matplotlib/47a57a5629a135f4301bf8181c5e244e1baf5759
/usr/share/package-licenses/pypi-matplotlib/81b71443d2a101a27194d8d7e0494a93e557a824
/usr/share/package-licenses/pypi-matplotlib/91cf189e02755085234dd321326345846bf2949f
/usr/share/package-licenses/pypi-matplotlib/920b5b7e7e79918ab41e714c4002f3ad4a8fdcfc
/usr/share/package-licenses/pypi-matplotlib/96cdc9c40477ab698d63b8c83fab29e2a8f72527
/usr/share/package-licenses/pypi-matplotlib/9fa4f855f33fa4ed73c9e6865d534a4f0f910610
/usr/share/package-licenses/pypi-matplotlib/fd0bb2832315e88d7a06dd4f28a73f4eac46d3c6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
