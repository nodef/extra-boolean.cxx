#pragma once

#include <iosfwd>
#include <string>

#include <extra-boolean/export.hxx>

namespace extra_boolean
{
  // Print a greeting for the specified name into the specified
  // stream. Throw std::invalid_argument if the name is empty.
  //
  EXTRA_BOOLEAN_SYMEXPORT void
  say_hello (std::ostream&, const std::string& name);
}
