#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/iostream.h>
#include <pybind11/operators.h>

#include <app/Roster.h>
#include <Entry.h>
#include <Messenger.h>
#include <OS.h>
#include <List.h>

namespace py = pybind11;


PYBIND11_MODULE(Roster,m)
{
m.attr("B_REQUEST_LAUNCHED") = 1;
m.attr("B_REQUEST_QUIT") = 2;
m.attr("B_REQUEST_ACTIVATED") = 4;

m.attr("B_SOME_APP_LAUNCHED") = py::int_('BRAS');
m.attr("B_SOME_APP_QUIT") = py::int_('BRAQ');
m.attr("B_SOME_APP_ACTIVATED") = py::int_('BRAW');

//m.attr("be_roster") = be_roster;

py::class_<app_info>(m, "app_info")
.def(py::init(), "")
.def_readwrite("thread", &app_info::thread)
.def_readwrite("team", &app_info::team)
.def_readwrite("port", &app_info::port)
.def_readwrite("flags", &app_info::flags)
.def_readwrite("ref", &app_info::ref)
.def_readonly("signature", &app_info::signature)
;

py::class_<BRoster>(m, "BRoster")
.def(py::init(), "")
.def("IsRunning", py::overload_cast<const char *>(&BRoster::IsRunning, py::const_), py::arg("signature"))
.def("IsRunning", py::overload_cast<entry_ref *>(&BRoster::IsRunning, py::const_), "", py::arg("ref"))
.def("TeamFor", py::overload_cast<const char *>(&BRoster::TeamFor, py::const_), py::arg("signature"))
.def("TeamFor", py::overload_cast<entry_ref *>(&BRoster::TeamFor, py::const_), py::arg("ref"))
.def("GetAppList", py::overload_cast<BList *>(&BRoster::GetAppList, py::const_), "", py::arg("teamIDList"))
.def("GetAppList", py::overload_cast<const char *, BList *>(&BRoster::GetAppList, py::const_), "", py::arg("signature"), py::arg("teamIDList"))
.def("GetAppInfo", py::overload_cast<const char *, app_info *>(&BRoster::GetAppInfo, py::const_), "", py::arg("signature"), py::arg("info"))
.def("GetAppInfo", py::overload_cast<entry_ref *, app_info *>(&BRoster::GetAppInfo, py::const_), "", py::arg("ref"), py::arg("info"))
.def("GetRunningAppInfo", &BRoster::GetRunningAppInfo, py::arg("team"), py::arg("info"))
.def("GetActiveAppInfo", &BRoster::GetActiveAppInfo, py::arg("info"))
.def("FindApp", py::overload_cast<const char *, entry_ref *>(&BRoster::FindApp, py::const_), "", py::arg("mimeType"), py::arg("app"))
.def("FindApp", py::overload_cast<entry_ref *, entry_ref *>(&BRoster::FindApp, py::const_), "", py::arg("ref"), py::arg("app"))
.def("Broadcast", py::overload_cast<BMessage *>(&BRoster::Broadcast, py::const_), "", py::arg("message"))
.def("Broadcast", py::overload_cast<BMessage *, BMessenger>(&BRoster::Broadcast, py::const_), "", py::arg("message"), py::arg("replyTo"))
.def("StartWatching", &BRoster::StartWatching, "", py::arg("target"), py::arg("eventMask")=B_REQUEST_LAUNCHED | B_REQUEST_QUIT)
.def("StopWatching", &BRoster::StopWatching, "", py::arg("target"))
.def("ActivateApp", &BRoster::ActivateApp, "", py::arg("team"))
.def("Launch", py::overload_cast<const char *, BMessage *, team_id *>(&BRoster::Launch, py::const_), "", py::arg("mimeType"), py::arg("initialMessage")=NULL, py::arg("_appTeam")=NULL)
.def("Launch", py::overload_cast<const char *, BList *, team_id *>(&BRoster::Launch, py::const_), "", py::arg("mimeType"), py::arg("messageList"), py::arg("_appTeam")=NULL)
//.def("Launch", py::overload_cast<const char *, int, const char * const *, team_id *>(&BRoster::Launch, py::const_), "", py::arg("mimeType"), py::arg("argc"), py::arg("args"), py::arg("_appTeam")=NULL)
.def("Launch", py::overload_cast<const entry_ref *, const BMessage *, team_id *>(&BRoster::Launch, py::const_), "", py::arg("ref"), py::arg("initialMessage")=NULL, py::arg("_appTeam")=NULL)
.def("Launch", py::overload_cast<const entry_ref *, const BList *, team_id *>(&BRoster::Launch, py::const_), "", py::arg("ref"), py::arg("messageList"), py::arg("_appTeam")=NULL)
//.def("Launch", py::overload_cast<const entry_ref *, int, const char * const *, team_id *>(&BRoster::Launch, py::const_), "", py::arg("ref"), py::arg("argc"), py::arg("args"), py::arg("_appTeam")=NULL)
.def("GetRecentDocuments", py::overload_cast<BMessage *, int32, const char *, const char *>(&BRoster::GetRecentDocuments, py::const_), "", py::arg("refList"), py::arg("maxCount"), py::arg("fileType")=NULL, py::arg("signature")=NULL)
//.def("GetRecentDocuments", py::overload_cast<BMessage *, int, const char *, int, const char *>(&BRoster::GetRecentDocuments), "", py::arg("refList"), py::arg("maxCount"), py::arg("fileTypes"), py::arg("fileTypesCount"), py::arg("signature")=NULL)
.def("GetRecentFolders", &BRoster::GetRecentFolders, "", py::arg("refList"), py::arg("maxCount"), py::arg("signature")=NULL)
.def("GetRecentApps", &BRoster::GetRecentApps, "", py::arg("refList"), py::arg("maxCount"))
.def("AddToRecentDocuments", &BRoster::AddToRecentDocuments, "", py::arg("document"), py::arg("signature")=NULL)
.def("AddToRecentFolders", &BRoster::AddToRecentFolders, "", py::arg("folder"), py::arg("signature")=NULL)
//.def_readonly("Private", &BRoster::Private)
;


}
