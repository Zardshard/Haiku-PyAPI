#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/iostream.h>
#include <pybind11/operators.h>

#include <app/PropertyInfo.h>
#include <BeBuild.h>
#include <Flattenable.h>
#include <SupportDefs.h>
#include <TypeConstants.h>
#include <Message.h>

namespace py = pybind11;


PYBIND11_MODULE(PropertyInfo,m)
{
py::enum_<value_kind>(m, "value_kind", "")
.value("B_COMMAND_KIND", value_kind::B_COMMAND_KIND, "")
.value("B_TYPE_CODE_KIND", value_kind::B_TYPE_CODE_KIND, "")
.export_values();

py::class_<compound_type>(m, "compound_type")
.def_readonly("pairs", &compound_type::pairs, "")
;

//py::class_<field_pair>(m, "field_pair")
//.def_readonly("name", &field_pair::name, "")
//.def_readonly("type", &field_pair::type, "")
//;

py::class_<property_info>(m, "property_info")
.def_readwrite("name", &property_info::name, "")
.def_readonly("commands", &property_info::commands, "")
.def_readonly("specifiers", &property_info::specifiers, "")
.def_readwrite("usage", &property_info::usage, "")
.def_readwrite("extra_data", &property_info::extra_data, "")
.def_readonly("types", &property_info::types, "")
.def_readonly("ctypes", &property_info::ctypes, "")
.def_readonly("_reserved", &property_info::_reserved, "")
;

py::class_<value_info>(m, "value_info")
.def_readwrite("name", &value_info::name, "")
.def_readwrite("value", &value_info::value, "")
.def_readwrite("kind", &value_info::kind, "")
.def_readwrite("usage", &value_info::usage, "")
.def_readwrite("extra_data", &value_info::extra_data, "")
.def_readonly("_reserved", &value_info::_reserved, "")
;

py::class_<BPropertyInfo>(m, "BPropertyInfo")
.def(py::init<property_info *, value_info *, bool>(), "", py::arg("prop")=NULL, py::arg("value")=NULL, py::arg("freeOnDelete")=false)
.def("FindMatch", &BPropertyInfo::FindMatch, "", py::arg("msg"), py::arg("index"), py::arg("specifier"), py::arg("form"), py::arg("prop"), py::arg("data")=NULL)
.def("IsFixedSize", &BPropertyInfo::IsFixedSize, "")
.def("TypeCode", &BPropertyInfo::TypeCode, "")
.def("FlattenedSize", &BPropertyInfo::FlattenedSize, "")
.def("Flatten", &BPropertyInfo::Flatten, "", py::arg("buffer"), py::arg("size"))
.def("AllowsTypeCode", &BPropertyInfo::AllowsTypeCode, "", py::arg("code"))
.def("Unflatten", &BPropertyInfo::Unflatten, "", py::arg("code"), py::arg("buffer"), py::arg("size"))
.def("Properties", &BPropertyInfo::Properties, "")
.def("Values", &BPropertyInfo::Values, "")
.def("CountProperties", &BPropertyInfo::CountProperties, "")
.def("CountValues", &BPropertyInfo::CountValues, "")
.def("PrintToStream", &BPropertyInfo::PrintToStream, "")
;


}
