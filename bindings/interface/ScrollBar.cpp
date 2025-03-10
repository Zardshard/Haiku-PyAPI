#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/iostream.h>
#include <pybind11/operators.h>

#include <interface/ScrollBar.h>
#include <View.h>

namespace py = pybind11;


PYBIND11_MODULE(ScrollBar,m)
{
py::class_<BScrollBar, BView>(m, "BScrollBar")
.def(py::init<BRect, const char *, BView *, float, float, orientation>(), "", py::arg("frame"), py::arg("name"), py::arg("target"), py::arg("min"), py::arg("max"), py::arg("direction"))
.def(py::init<const char *, BView *, float, float, orientation>(), "", py::arg("name"), py::arg("target"), py::arg("min"), py::arg("max"), py::arg("orientation"))
.def(py::init<BMessage *>(), "", py::arg("archive"))
.def_static("Instantiate", &BScrollBar::Instantiate, "", py::arg("archive"))
.def("Archive", &BScrollBar::Archive, "", py::arg("archive"), py::arg("deep")=true)
.def("AllAttached", &BScrollBar::AllAttached, "")
.def("AllDetached", &BScrollBar::AllDetached, "")
.def("AttachedToWindow", &BScrollBar::AttachedToWindow, "")
.def("DetachedFromWindow", &BScrollBar::DetachedFromWindow, "")
.def("Draw", &BScrollBar::Draw, "", py::arg("updateRect"))
.def("FrameMoved", &BScrollBar::FrameMoved, "", py::arg("new_position"))
.def("FrameResized", &BScrollBar::FrameResized, "", py::arg("newWidth"), py::arg("newHeight"))
.def("MessageReceived", &BScrollBar::MessageReceived, "", py::arg("message"))
.def("MouseDown", &BScrollBar::MouseDown, "", py::arg("where"))
.def("MouseUp", &BScrollBar::MouseUp, "", py::arg("where"))
.def("MouseMoved", &BScrollBar::MouseMoved, "", py::arg("where"), py::arg("code"), py::arg("dragMessage"))
.def("WindowActivated", &BScrollBar::WindowActivated, "", py::arg("active"))
.def("SetValue", &BScrollBar::SetValue, "", py::arg("value"))
.def("Value", &BScrollBar::Value, "")
.def("SetProportion", &BScrollBar::SetProportion, "", py::arg(""))
.def("Proportion", &BScrollBar::Proportion, "")
.def("ValueChanged", &BScrollBar::ValueChanged, "", py::arg("newValue"))
.def("SetRange", &BScrollBar::SetRange, "", py::arg("min"), py::arg("max"))
.def("GetRange", &BScrollBar::GetRange, "", py::arg("_min"), py::arg("_max"))
.def("SetSteps", &BScrollBar::SetSteps, "", py::arg("smallStep"), py::arg("largeStep"))
.def("GetSteps", &BScrollBar::GetSteps, "", py::arg("_smallStep"), py::arg("_largeStep"))
.def("SetTarget", py::overload_cast<BView *>(&BScrollBar::SetTarget), "", py::arg("target"))
.def("SetTarget", py::overload_cast<const char *>(&BScrollBar::SetTarget), "", py::arg("targetName"))
.def("Target", &BScrollBar::Target, "")
.def("SetOrientation", &BScrollBar::SetOrientation, "", py::arg("direction"))
.def("Orientation", &BScrollBar::Orientation, "")
.def("SetBorderHighlighted", &BScrollBar::SetBorderHighlighted, "", py::arg("highlight"))
.def("GetPreferredSize", &BScrollBar::GetPreferredSize, "", py::arg("_width"), py::arg("_height"))
.def("ResizeToPreferred", &BScrollBar::ResizeToPreferred, "")
.def("MakeFocus", &BScrollBar::MakeFocus, "", py::arg("focus")=true)
.def("MinSize", &BScrollBar::MinSize, "")
.def("MaxSize", &BScrollBar::MaxSize, "")
.def("PreferredSize", &BScrollBar::PreferredSize, "")
.def("GetSupportedSuites", &BScrollBar::GetSupportedSuites, "", py::arg("message"))
.def("ResolveSpecifier", &BScrollBar::ResolveSpecifier, "", py::arg("message"), py::arg("index"), py::arg("specifier"), py::arg("what"), py::arg("property"))
.def("Perform", &BScrollBar::Perform, "", py::arg("d"), py::arg("arg"))
;


}
