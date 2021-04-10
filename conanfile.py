from conans import ConanFile

class ExtraBoolean(ConanFile):
  name = "extra-boolean"
  version = "0.0"
  license = "MIT"
  url = "https://conan.io/center/extra-boolean"
  homepage = "https://github.com/cppf/extra-boolean"
  description = "Boolean data type has two possible truth values to represent logic."
  topics = ("extra", "boolean", "algebra", "logic", "parse", "not", "eq", "neq", "imply", "nimply", "and", "or", "xor", "count", "nand", "nor", "xnor", "select")
  exports_sources = "include/*"
  no_copy_source = True

  def package(self):
    self.copy("*.h")

# picojson recipe
# url: https://github.com/conan-io/conan-center-index/blob/7a34d7b321de8455b1697c803a38086b208674e5/recipes/picojson/all/conanfile.py
# homepage: https://github.com/kazuho/picojson
# _source_subdir_name = "source_subdir"

# def source(self):
#   tools.get(**self.conan_data["sources"][self.version])
#   os.rename("picojson-{}".format(self.version), self._source_subdir_name)

# def package(self):
#   self.copy("{}.h".format(self.name), dst="include", src=self._source_subdir_name)
#   self.copy("LICENSE", dst="licenses", src=self._source_subdir_name)

# def package_info(self):
#   self.info.header_only()
