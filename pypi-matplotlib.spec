#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v20
# autospec commit: f35655a
#
Name     : pypi-matplotlib
Version  : 3.8.4
Release  : 132
URL      : https://files.pythonhosted.org/packages/38/4f/8487737a74d8be4ab5fbe6019b0fae305c1604cf7209500969b879b5f462/matplotlib-3.8.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/38/4f/8487737a74d8be4ab5fbe6019b0fae305c1604cf7209500969b879b5f462/matplotlib-3.8.4.tar.gz
Summary  : Python plotting package
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause CC-BY-4.0 CC0-1.0 HPND MIT OFL-1.0 OFL-1.1 Python-2.0
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
BuildRequires : pypi(kiwisolver)
BuildRequires : pypi(numpy)
BuildRequires : pypi(pillow)
BuildRequires : pypi(py)
BuildRequires : pypi(pybind11)
BuildRequires : pypi(pyparsing)
BuildRequires : pypi(python_dateutil)
BuildRequires : pypi(pytz)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(tornado)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
BuildRequires : python3-tcl
BuildRequires : qhull-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![PyPi](https://img.shields.io/pypi/v/matplotlib)](https://pypi.org/project/matplotlib/)
[![Conda](https://img.shields.io/conda/vn/conda-forge/matplotlib)](https://anaconda.org/conda-forge/matplotlib)
[![Downloads](https://img.shields.io/pypi/dm/matplotlib)](https://pypi.org/project/matplotlib)
[![NUMFocus](https://img.shields.io/badge/powered%20by-NumFOCUS-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://numfocus.org)

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
Requires: python3-core
Provides: pypi(matplotlib)
Requires: cycler
Requires: pypi(contourpy)
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
%setup -q -n matplotlib-3.8.4
cd %{_builddir}/matplotlib-3.8.4
pushd ..
cp -a matplotlib-3.8.4 buildavx2
popd

%build
## build_prepend content
sed -e 's|#system_freetype = False|system_freetype = True|' -e 's|#system_qhull = False|system_qhull = True|' mplsetup.cfg.template > mplsetup.cfg
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1730219508
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . pyparsing
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
## build_prepend content
sed -e 's|#system_freetype = False|system_freetype = True|' -e 's|#system_qhull = False|system_qhull = True|' mplsetup.cfg.template > mplsetup.cfg
## build_prepend end
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
pypi-dep-fix.py . pyparsing
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-matplotlib
cp %{_builddir}/matplotlib-%{version}/LICENSE/LICENSE %{buildroot}/usr/share/package-licenses/pypi-matplotlib/3683efd59fb44e798efb22fd086a5b1e3a0aa700 || :
cp %{_builddir}/matplotlib-%{version}/LICENSE/LICENSE_AMSFONTS %{buildroot}/usr/share/package-licenses/pypi-matplotlib/91cf189e02755085234dd321326345846bf2949f || :
cp %{_builddir}/matplotlib-%{version}/LICENSE/LICENSE_BAKOMA %{buildroot}/usr/share/package-licenses/pypi-matplotlib/9fa4f855f33fa4ed73c9e6865d534a4f0f910610 || :
cp %{_builddir}/matplotlib-%{version}/LICENSE/LICENSE_COLORBREWER %{buildroot}/usr/share/package-licenses/pypi-matplotlib/032b9dc00790fcac1f05bcc7627b1572e4dbc09a || :
cp %{_builddir}/matplotlib-%{version}/LICENSE/LICENSE_JSXTOOLS_RESIZE_OBSERVER %{buildroot}/usr/share/package-licenses/pypi-matplotlib/920b5b7e7e79918ab41e714c4002f3ad4a8fdcfc || :
cp %{_builddir}/matplotlib-%{version}/LICENSE/LICENSE_QT4_EDITOR %{buildroot}/usr/share/package-licenses/pypi-matplotlib/04bb73e33817fa6c0c1259344f7326b408e12885 || :
cp %{_builddir}/matplotlib-%{version}/LICENSE/LICENSE_SOLARIZED %{buildroot}/usr/share/package-licenses/pypi-matplotlib/81b71443d2a101a27194d8d7e0494a93e557a824 || :
cp %{_builddir}/matplotlib-%{version}/LICENSE/LICENSE_YORICK %{buildroot}/usr/share/package-licenses/pypi-matplotlib/fd0bb2832315e88d7a06dd4f28a73f4eac46d3c6 || :
cp %{_builddir}/matplotlib-%{version}/doc/_static/fa/LICENSE %{buildroot}/usr/share/package-licenses/pypi-matplotlib/38f5fae1676b8f00409b0fb2979799ed35320999 || :
cp %{_builddir}/matplotlib-%{version}/doc/devel/license.rst %{buildroot}/usr/share/package-licenses/pypi-matplotlib/96cdc9c40477ab698d63b8c83fab29e2a8f72527 || :
cp %{_builddir}/matplotlib-%{version}/extern/agg24-svn/src/copying %{buildroot}/usr/share/package-licenses/pypi-matplotlib/467189783f672de8baca8b34e798fa2da64166a5 || :
cp %{_builddir}/matplotlib-%{version}/lib/matplotlib/mpl-data/fonts/ttf/LICENSE_DEJAVU %{buildroot}/usr/share/package-licenses/pypi-matplotlib/23e8fed3e3499427ef5a80cbff0aca0946140493 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
pypi-dep-fix.py %{buildroot} pyparsing
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-matplotlib/032b9dc00790fcac1f05bcc7627b1572e4dbc09a
/usr/share/package-licenses/pypi-matplotlib/04bb73e33817fa6c0c1259344f7326b408e12885
/usr/share/package-licenses/pypi-matplotlib/23e8fed3e3499427ef5a80cbff0aca0946140493
/usr/share/package-licenses/pypi-matplotlib/3683efd59fb44e798efb22fd086a5b1e3a0aa700
/usr/share/package-licenses/pypi-matplotlib/38f5fae1676b8f00409b0fb2979799ed35320999
/usr/share/package-licenses/pypi-matplotlib/467189783f672de8baca8b34e798fa2da64166a5
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
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
