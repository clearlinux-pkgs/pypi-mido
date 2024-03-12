#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v4
# autospec commit: 3d985eb
#
Name     : pypi-mido
Version  : 1.3.2
Release  : 72
URL      : https://files.pythonhosted.org/packages/9e/a4/f9bfc7016c9fb1e348078a3455ab0d1573bcb5154dc7fc1aba9fcfe38b95/mido-1.3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/9e/a4/f9bfc7016c9fb1e348078a3455ab0d1573bcb5154dc7fc1aba9fcfe38b95/mido-1.3.2.tar.gz
Summary  : MIDI Objects for Python
Group    : Development/Tools
License  : CC0-1.0 MIT
Requires: pypi-mido-bin = %{version}-%{release}
Requires: pypi-mido-license = %{version}-%{release}
Requires: pypi-mido-python = %{version}-%{release}
Requires: pypi-mido-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
..
.. SPDX-License-Identifier: CC-BY-4.0
Mido - MIDI Objects for Python
==============================

%package bin
Summary: bin components for the pypi-mido package.
Group: Binaries
Requires: pypi-mido-license = %{version}-%{release}

%description bin
bin components for the pypi-mido package.


%package license
Summary: license components for the pypi-mido package.
Group: Default

%description license
license components for the pypi-mido package.


%package python
Summary: python components for the pypi-mido package.
Group: Default
Requires: pypi-mido-python3 = %{version}-%{release}

%description python
python components for the pypi-mido package.


%package python3
Summary: python3 components for the pypi-mido package.
Group: Default
Requires: python3-core
Provides: pypi(mido)
Requires: pypi(packaging)

%description python3
python3 components for the pypi-mido package.


%prep
%setup -q -n mido-1.3.2
cd %{_builddir}/mido-1.3.2
pushd ..
cp -a mido-1.3.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710250778
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
pypi-dep-fix.py . packaging
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
pypi-dep-fix.py . packaging
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-mido
cp %{_builddir}/mido-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-mido/d891cc509267ee382f3cf7389f1c6f6304954ec7 || :
cp %{_builddir}/mido-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/pypi-mido/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/mido-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/pypi-mido/adadb67a9875aeeac285309f1eab6e47d9ee08a7 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
pypi-dep-fix.py %{buildroot} packaging
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

%files bin
%defattr(-,root,root,-)
/usr/bin/mido-connect
/usr/bin/mido-play
/usr/bin/mido-ports
/usr/bin/mido-serve

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-mido/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/pypi-mido/adadb67a9875aeeac285309f1eab6e47d9ee08a7
/usr/share/package-licenses/pypi-mido/d891cc509267ee382f3cf7389f1c6f6304954ec7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
