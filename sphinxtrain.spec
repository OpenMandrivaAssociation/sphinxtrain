Name: sphinxtrain
Version: 1.0.7
Release: %mkrel 0
Summary: An acoustic model trainer for CMU's Sphinx tools
Group: Development/Other
License: BSD and LGPLv2+
URL: http://www.cmusphinx.org/
Source: http://downloads.sourceforge.net/cmusphinx/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires: sphinxbase-devel, python-devel, python-setuptools, python-scipy

%description
SphinxTrain is Carnegie Mellon University's open source acoustic model
trainer.  It contains the scripts and instructions necessary for building
models for the CMU Sphinx Recognizer.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %{buildroot}
export BDIR=`pwd`
mkdir -p %{buildroot}%{_libdir}/%{name}
cd %{buildroot}%{_libdir}/%{name}
$BDIR/scripts_pl/setup_SphinxTrain.pl -task Mandriva

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README NEWS
%doc doc/s3_fe_spec.pdf doc/tinydoc.txt
%{_libdir}/%{name}
