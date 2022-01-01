#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fAssets
Version  : 3042.84
Release  : 33
URL      : https://cran.r-project.org/src/contrib/fAssets_3042.84.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fAssets_3042.84.tar.gz
Summary  : Rmetrics - Analysing and Modelling Financial Assets
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-ecodist
Requires: R-energy
Requires: R-fBasics
Requires: R-fMultivar
Requires: R-mvnormtest
Requires: R-robustbase
Requires: R-sn
Requires: R-timeDate
Requires: R-timeSeries
BuildRequires : R-ecodist
BuildRequires : R-energy
BuildRequires : R-fBasics
BuildRequires : R-fMultivar
BuildRequires : R-mvnormtest
BuildRequires : R-robustbase
BuildRequires : R-sn
BuildRequires : R-timeDate
BuildRequires : R-timeSeries
BuildRequires : buildreq-R

%description
to manage, to investigate and to analyze data sets of financial 
  assets from different points of view.

%prep
%setup -q -c -n fAssets
cd %{_builddir}/fAssets

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641011543

%install
export SOURCE_DATE_EPOCH=1641011543
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fAssets
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fAssets
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fAssets
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fAssets || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fAssets/DESCRIPTION
/usr/lib64/R/library/fAssets/INDEX
/usr/lib64/R/library/fAssets/Meta/Rd.rds
/usr/lib64/R/library/fAssets/Meta/features.rds
/usr/lib64/R/library/fAssets/Meta/hsearch.rds
/usr/lib64/R/library/fAssets/Meta/links.rds
/usr/lib64/R/library/fAssets/Meta/nsInfo.rds
/usr/lib64/R/library/fAssets/Meta/package.rds
/usr/lib64/R/library/fAssets/NAMESPACE
/usr/lib64/R/library/fAssets/R/fAssets
/usr/lib64/R/library/fAssets/R/fAssets.rdb
/usr/lib64/R/library/fAssets/R/fAssets.rdx
/usr/lib64/R/library/fAssets/help/AnIndex
/usr/lib64/R/library/fAssets/help/aliases.rds
/usr/lib64/R/library/fAssets/help/fAssets.rdb
/usr/lib64/R/library/fAssets/help/fAssets.rdx
/usr/lib64/R/library/fAssets/help/paths.rds
/usr/lib64/R/library/fAssets/html/00Index.html
/usr/lib64/R/library/fAssets/html/R.css
/usr/lib64/R/library/fAssets/obsolete/a-class-fASSETS.R
/usr/lib64/R/library/fAssets/obsolete/a-class-fASSETS.Rd
/usr/lib64/R/library/fAssets/obsolete/assets-modeling.Rd
