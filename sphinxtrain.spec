Name: sphinxtrain
Version: 1.0.7
Release: %mkrel 2
Summary: An acoustic model trainer for CMU's Sphinx tools
Group: Development/Other
License: BSD and LGPLv2+
URL: http://www.cmusphinx.org/
Source: http://downloads.sourceforge.net/cmusphinx/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Requires: sphinxbase
BuildRequires: sphinxbase-devel, python-devel, python-setuptools, python-scipy
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


%changelog
* Thu Apr 28 2011 zamir <zamir@mandriva.org> 1.0.7-2mdv2011.0
+ Revision: 659861
- new sphinxtrain requires sphinxbase

* Thu Apr 28 2011 zamir <zamir@mandriva.org> 1.0.7-1
+ Revision: 659854
- fix LDA train bug
- fix LDA train bug

* Wed Apr 20 2011 zamir <zamir@mandriva.org> 1.0.7-0
+ Revision: 656316
- rebuild with new sphinxbase realese
- new realese
- new realese
- new realese

* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-2
+ Revision: 645889
- relink against libmysqlclient.so.18

* Sat Nov 27 2010 Eugeni Dodonov <eugeni@mandriva.com> 1.0-1mdv2011.0
+ Revision: 601628
- fix package name
- Simplify %%build and %%install sections.
  Updated Group.

  + zamir <zamir@mandriva.org>
    - first build
    - Created package structure for sphinxtrain.

