%define debug_package %{nil}
%define _build_id_links none
%define service_user {{ cookiecutter.project_name }}

Name:       {{ cookiecutter.project_name }}
Version:    {{ cookiecutter.version }}
Release:    1%{?dist}
Summary:    {{ cookiecutter.project_name }}

License:    {{ cookiecutter.license }}
URL:        {{ cookiecutter.project_url }}
AutoReqProv: no
Source0:    %{name}-%{version}.tar.gz
BuildRequires: systemd-rpm-macros
BuildRequires: python38 >= 3.8
BuildRequires: pkgconfig(python-3.8) >= 3.8
BuildRequires: postgresql-devel
BuildRequires: libffi-devel

Requires: python38 >= 3.8
Requires: pkgconfig(pythoni-3.8) >= 3.8
Requires: postgresql-libs postgresql 
Requires: libffi

Requires(pre): /usr/sbin/useradd, /usr/bin/getent
Requires(postun): /usr/sbin/userdel

%description
{{ cookiecutter.project_name }}

%prep
rm -rf %{_builddir}/%{name}/
%setup -q -b 0 -n %{name}

%build
rm -rf $RPM_BUILD_ROOT

%install
mkdir -p ${RPM_BUILD_ROOT}/%{_bindir}/
mkdir -p ${RPM_BUILD_ROOT}/opt/%{name}/
cp -r %{name} ${RPM_BUILD_ROOT}/opt/%{name}/
cp -r migrations ${RPM_BUILD_ROOT}/opt/%{name}/
cp *.cfg ${RPM_BUILD_ROOT}/opt/%{name}/
cp *.rst ${RPM_BUILD_ROOT}/opt/%{name}/
cp build.sh ${RPM_BUILD_ROOT}/opt/%{name}/
cp setup.py ${RPM_BUILD_ROOT}/opt/%{name}/
cp MANIFEST.in ${RPM_BUILD_ROOT}/opt/%{name}/

cp .mr.developer.cfg .mfwtemplaterc ${RPM_BUILD_ROOT}/opt/%{name}/
pushd ${RPM_BUILD_ROOT}/opt/%{name}/
./build.sh -c buildout-rpm.cfg
popd

# create resource dirs
mkdir -p ${RPM_BUILD_ROOT}/%{_localstatedir}/log/%{name}/
mkdir -p ${RPM_BUILD_ROOT}/%{_sharedstatedir}/%{name}/blobstorage
mkdir -p ${RPM_BUILD_ROOT}/%{_sysconfdir}/logrotate.d/
mkdir -p ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}/
mkdir -p ${RPM_BUILD_ROOT}/%{_unitdir}/

# settings file
cp settings.yml ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}/settings.yml
cp alembic.ini ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}/alembic.ini

sed -i \
    's|script_location = migrations|script_location = /opt/%{name}/migrations|g' \
    ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}/alembic.ini

sed -i \
    "s|fsblob://\%%(here)s/blobstorage|fsblob:///%{_sharedstatedir}/%{name}/blobstorage|g" \
    ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}/settings.yml

# logrotate config
cp etc/logrotate.conf ${RPM_BUILD_ROOT}/%{_sysconfdir}/logrotate.d/%{name}

# systemd config
cp etc/web.service ${RPM_BUILD_ROOT}/%{_unitdir}/%{name}-web.service
cp etc/worker.service ${RPM_BUILD_ROOT}/%{_unitdir}/%{name}-worker.service
cp etc/scheduler.service ${RPM_BUILD_ROOT}/%{_unitdir}/%{name}-scheduler.service

# management script 
cat > ${RPM_BUILD_ROOT}/%{_bindir}/%{name} << EOF
#!/bin/bash
export ALEMBIC_CONFIG=%{_sysconfdir}/%{name}/alembic.ini
export MFW_CONFIG=%{_sysconfdir}/%{name}/settings.yml

/opt/%{name}/bin/morpfw \$@

EOF

# strip rpmbuildroot paths
grep -lrZF "#!$RPM_BUILD_ROOT" $RPM_BUILD_ROOT | xargs -r -0 perl -p -i -e "s|$RPM_BUILD_ROOT||g"
find $RPM_BUILD_ROOT -type f -regex '.*egg-link$' |xargs -I% grep -lrZF "$RPM_BUILD_ROOT" % | xargs -r -0 perl -p -i -e "s|$RPM_BUILD_ROOT||g"
grep -lrZF "$RPM_BUILD_ROOT" $RPM_BUILD_ROOT/opt/%{name}/bin/ | xargs -r -0 perl -p -i -e "s|$RPM_BUILD_ROOT||g"
grep -lrZF "$RPM_BUILD_ROOT" $RPM_BUILD_ROOT/opt/%{name}/venv/bin/ | xargs -r -0 perl -p -i -e "s|$RPM_BUILD_ROOT||g"

# cleanup
rm ${RPM_BUILD_ROOT}/opt/%{name}/.installed.cfg
find ${RPM_BUILD_ROOT} -regex '.*\.pyc$' -exec rm '{}' ';'
find ${RPM_BUILD_ROOT} -regex '.*\.pyo$' -exec rm '{}' ';'


%post
/opt/%{name}/venv/bin/python -m compileall -q /opt/%{name}/ > /dev/null 2>&1 
/usr/bin/systemctl daemon-reload
%systemd_post %{name}-web.service
%systemd_post %{name}-scheduler.service
%systemd_post %{name}-worker.service


%preun
%systemd_preun %{name}-web.service
%systemd_preun %{name}-scheduler.service
%systemd_preun %{name}-worker.service

%postun
%systemd_postun_with_restart %{name}-web.service
%systemd_postun_with_restart %{name}-scheduler.service
%systemd_postun_with_restart %{name}-worker.service
/usr/bin/systemctl daemon-reload

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/usr/bin/getent group %{service_user} >/dev/null || /usr/sbin/groupadd -r %{service_user}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd -r \
     -g %{service_user} -d /opt/%{name}/ -s /sbin/nologin %{service_user}

%files
%defattr(644, root, root ,755)
%attr(755,-,-) /opt/%{name}/build.sh
%config %attr(644, %{service_user},%{service_user}) %{_sysconfdir}/%{name}/settings.yml
%config %attr(644, %{service_user},%{service_user}) %{_sysconfdir}/%{name}/alembic.ini
%config %{_sysconfdir}/logrotate.d/%{name}

/opt/%{name}/*.cfg
/opt/%{name}/*.py
/opt/%{name}/*.rst
/opt/%{name}/MANIFEST.in
/opt/%{name}/migrations/
/opt/%{name}/%{name}/
/opt/%{name}/%{name}.egg-info/
/opt/%{name}/eggs/
/opt/%{name}/develop-eggs/
/opt/%{name}/dev/
/opt/%{name}/parts/
/opt/%{name}/venv/lib*
/opt/%{name}/venv/include/
/opt/%{name}/venv/*.cfg
/opt/%{name}/.mfwtemplaterc
/opt/%{name}/.mr.developer.cfg
%attr(755,-,-) /opt/%{name}/bin/*
%attr(755,-,-) %{_bindir}/%{name}
/opt/%{name}/venv/bin/python
/opt/%{name}/venv/bin/python3*
%attr(755,-,-) /opt/%{name}/venv/bin/python.sh
%attr(755,-,-) /opt/%{name}/venv/bin/buildout
%attr(755,-,-) /opt/%{name}/venv/bin/easy_install*
%attr(755,-,-) /opt/%{name}/venv/bin/pip*
/opt/%{name}/venv/bin/activate*
/opt/%{name}/venv/bin/Activate*
%{_unitdir}/%{name}-web.service
%{_unitdir}/%{name}-scheduler.service
%{_unitdir}/%{name}-worker.service
%attr(755,%{service_user},%{service_user}) %{_localstatedir}/log/%{name}
%dir %attr(755,%{service_user},%{service_user}) %{_sharedstatedir}/%{name}
%dir %attr(755,%{service_user},%{service_user}) %{_sharedstatedir}/%{name}/blobstorage

%changelog

* {{ cookiecutter.rpm_date }} {{ cookiecutter.author_name }} {{ cookiecutter.version }}
- initial package
