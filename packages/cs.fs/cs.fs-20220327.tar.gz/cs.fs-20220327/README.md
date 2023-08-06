Assorted filesystem related utility functions,
some of which have been bloating cs.fileutils for too long.

*Latest release 20220327*:
New module cs.fs to contain more filesystem focussed functions than cs.fileutils, which is feeling a bit bloated.

## Function `atomic_directory(*da, **dkw)`

Decorator for a function which fills in a directory
which calls the function against a temporary directory
then renames the temporary to the target name on completion.

Parameters:
* `infill_func`: the function to fill in the target directory
* `make_placeholder`: optional flag, default `False`:
  if true an empty directory will be make at the target name
  and after completion it will be removed and the completed
  directory renamed to the target name

## Function `rpaths(dirpath='.', *, only_suffixes=None, skip_suffixes=None, sort_paths=False)`

Yield relative file paths from a directory.

Parameters:
* `dirpath`: optional top directory, default `'.'`
* `only_suffixes`: optional iterable of suffixes of interest;
  if provided only files ending in these suffixes will be yielded
* `skip_suffixes`: optional iterable if suffixes to ignore;
  if provided files ending in these suffixes will not be yielded
* `sort_paths`: optional flag specifying that filenames should be sorted,
  default `False`

# Release Log



*Release 20220327*:
New module cs.fs to contain more filesystem focussed functions than cs.fileutils, which is feeling a bit bloated.
