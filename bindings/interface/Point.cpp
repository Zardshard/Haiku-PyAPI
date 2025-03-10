#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/iostream.h>
#include <pybind11/operators.h>

#include <interface/Point.h>
#include <SupportDefs.h>

namespace py = pybind11;


PYBIND11_MODULE(Point,m)
{
m.attr("B_ORIGIN") = B_ORIGIN;

py::class_<BPoint>(m, "BPoint")
.def(py::init(), "")
.def(py::init<float, float>(), "", py::arg("x"), py::arg("y"))
.def(py::init<const BPoint &>(), "", py::arg("p"))
.def("operator=", &BPoint::operator=, "", py::arg("other"))
.def("Set", &BPoint::Set, "", py::arg("x"), py::arg("y"))
.def("ConstrainTo", &BPoint::ConstrainTo, "", py::arg("rect"))
.def("PrintToStream", &BPoint::PrintToStream, "")
.def("operator-", py::overload_cast<>(&BPoint::operator-), "")
.def("__add__", &BPoint::operator+, "", py::arg("other"))
.def("operator-", py::overload_cast<const BPoint &>(&BPoint::operator-), "", py::arg("other"))
.def("__iadd__", &BPoint::operator+=, "", py::arg("other"))
.def("__isub__", &BPoint::operator-=, "", py::arg("other"))
.def("__ne__", &BPoint::operator!=, "", py::arg("other"))
.def("__eq__", &BPoint::operator==, "", py::arg("other"))
.def_readwrite("x", &BPoint::x, "")
.def_readwrite("y", &BPoint::y, "")
;

m.def("operator=", &operator=, "", py::arg("other"));

}
