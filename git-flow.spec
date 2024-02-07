# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: git-flow
Epoch: 100
Version: 1.12.3
Release: 1%{?dist}
Summary: Git extension to provide a high-level branching model
License: LGPL-2.1-or-later
URL: https://github.com/petervanderdoes/gitflow-avh/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: git
Requires: git

%description
A set of scripts that provide high-level repository operations for
managing feature/release/hotfix branches in a Git repository,
particularly suited to be utilised to follow Vincent Driessen's
branching model, described at
<https://nvie.com/posts/a-successful-git-branching-model/>.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build

%install
install -Dpm755 -d %{buildroot}%{_bindir}
install -Dpm755 -d %{buildroot}%{_datadir}/bash-completion/completions
install -Dpm755 -d %{buildroot}%{_docdir}/git-flow/hooks
install -Dpm755 -t %{buildroot}%{_bindir} git-flow
install -Dpm644 -t %{buildroot}%{_bindir} git-flow-bugfix
install -Dpm644 -t %{buildroot}%{_bindir} git-flow-config
install -Dpm644 -t %{buildroot}%{_bindir} git-flow-feature
install -Dpm644 -t %{buildroot}%{_bindir} git-flow-hotfix
install -Dpm644 -t %{buildroot}%{_bindir} git-flow-init
install -Dpm644 -t %{buildroot}%{_bindir} git-flow-log
install -Dpm644 -t %{buildroot}%{_bindir} git-flow-release
install -Dpm644 -t %{buildroot}%{_bindir} git-flow-support
install -Dpm644 -t %{buildroot}%{_bindir} git-flow-version
install -Dpm644 -t %{buildroot}%{_bindir} gitflow-common
install -Dpm644 -t %{buildroot}%{_bindir} gitflow-shFlags
cp -rfp git-flow-completion.bash %{buildroot}%{_datadir}/bash-completion/completions/git-flow
chmod 644 %{buildroot}%{_datadir}/bash-completion/completions/git-flow
cp -rfp hooks/* %{buildroot}%{_docdir}/git-flow/hooks
chmod 644 %{buildroot}%{_docdir}/git-flow/hooks/*

%files
%license LICENSE
%dir %{_docdir}/git-flow
%dir %{_docdir}/git-flow/hooks
%{_bindir}/git-flow
%{_bindir}/git-flow-bugfix
%{_bindir}/git-flow-config
%{_bindir}/git-flow-feature
%{_bindir}/git-flow-hotfix
%{_bindir}/git-flow-init
%{_bindir}/git-flow-log
%{_bindir}/git-flow-release
%{_bindir}/git-flow-support
%{_bindir}/git-flow-version
%{_bindir}/gitflow-common
%{_bindir}/gitflow-shFlags
%{_datadir}/bash-completion/completions/git-flow
%{_docdir}/git-flow/hooks/*

%changelog
