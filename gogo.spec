Summary:       MP3 encoder based on lame
Summary(pl):   Program do kompresji plik�w MP3 stworzony na podstawie programu lame
Name:          gogo
Version:       224b
Release:       1
Copyright:     GPL
Group:         Applications/Sound
Group(pl):     Aplikacje/D�wi�k
Source:        %{name}%{version}.tar.gz
Buildroot:     /tmp/%{name}-%{version}-root

%description
This software is based lame MP3 encoder. GOGO can encode about TWICE as
fast as original LAME can on K6-2 315MHz, and its quality is the about same
as LAME's. GOGO makes use of MMX, (Enhanced) 3D Now! and SSE if your system
supports these units.

%description -l pl
GOGO jest programem do kompresji plik�w MP3, kt�ry zosta� stworzony
na podstawie programu lame. Program ten potrafi by� dwa razy szybszy
od orygina�u w systemie z procesorem K6-2 315MHz, zachowuj�c jednocze�nie
jako�� kompresowanych plik�w. GOGO wykorzystuje MMX, instrukcje 3D Now!
oraz SSE.

%prep
%setup -q -n %{name}%{version}

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
strip gogo

# binary files
install -d $RPM_BUILD_ROOT%{_prefix}
install gogo $RPM_BUILD_ROOT%{_prefix}

gzip -9nf COPYING readme.txt readme_e.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc {COPYING,readme.txt,readme_e.txt}.gz
%attr(755, root, root) %{_prefix}/gogo
