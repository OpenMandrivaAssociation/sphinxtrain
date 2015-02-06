Name:     sphinxtrain
Version:  1.0.7
Release:  4
Summary:  An acoustic model trainer for CMU's Sphinx tools
Group:    Development/Other
License:  BSD and LGPLv2+
URL:      http://www.cmusphinx.org/
Source:   http://downloads.sourceforge.net/cmusphinx/%{name}-%{version}.tar.gz
Requires: sphinxbase
BuildRequires: sphinxbase-devel
BuildRequires: python-devel
BuildRequires: python-setuptools
BuildRequires: python-scipy
BuildRequires: pkgconfig(sndfile)
Patch0: sphinxtrain.patch

%description
SphinxTrain is Carnegie Mellon University's open source acoustic model
trainer.  It contains the scripts and instructions necessary for building
models for the CMU Sphinx Recognizer.

%prep
%setup -q
%patch0 -p1 -b .lda

%build
%configure
%make

%install
export BDIR=`pwd`
mkdir -p %{buildroot}%{_libdir}/%{name}
cd %{buildroot}%{_libdir}/%{name}
$BDIR/scripts_pl/setup_SphinxTrain.pl -task Mandriva

%files
%doc COPYING README NEWS
%doc doc/s3_fe_spec.pdf doc/tinydoc.txt
%{_libdir}/%{name}
