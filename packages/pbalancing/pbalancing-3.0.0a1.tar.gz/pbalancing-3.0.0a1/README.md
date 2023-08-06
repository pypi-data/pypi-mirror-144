# Parameter Balancing: Standalone Version

Parameter balancing is a tool for metabolic modeling in systems biology. It is implemented in Python and its code underlies the PEP8 guidelines. It can either be downloaded and used from command-line as is or embedded in your own Python3 projects. In both cases, you will be required to install Python packages to make the scripts work.

## Parameter balancing on the command-line

Parameter balancing can be employed on the command-line by
```bash
python -m scripts.parameter_balancing.py model.xml
```

where `model.xml` corresponds to the path of your SBML model. It is also possible to provide further input files, such as
an SBtab parameter files (`.tsv`), an SBtab prior information file (`.tsv`), and an SBtab options file (`.tsv`) for the
configuration of parameter balancing. Providing complete file information would look like this:

```bash
python -m scripts.parameter_balancing.py model.xml --sbtab_data data_file.tsv --sbtab_prior prior_file.tsv --sbtab_options options_file.tsv
```

You can create a log file by setting the flag -l, you can use pseudo values to account for a lack of data by setting the flag -p, you can watch program outputs on your command-line by setting the flag -v. Information on the SBtab format can be found on `www.sbtab.net`, more information on the mentioned file types can be found in the parameter balancing manual in this repository's `examples/pb_manual.pdf`, and example files can be found in `examples/example_files/`.

## Embedding parameter balancing in your Python package

You can also embed the modules of parameter balancing in your own Python workflow.

```python
from pbalancing import parameter_balancing_wrapper

balanced_sbml, balanced_sbtab = parameter_balancing_wrapper(
  sbml,
  sbtab_data,
  sbtab_prior,
  sbtab_options,
  verbose,
  no_pseudo_values,
  output_name,
  pb_log
)
```

### Input arguments
  - `sbml` - path to SBML file, REQUIRED)
  - `sbtab_data` - path to SBtab data file (OPTIONAL)
  - `sbtab_prior` - path to SBtab prior file (OPTIONAL)
  - `sbtab_options` - path to SBtab options file (OPTIONAL)
  - `verbose` - Boolean, enable messages on command-line (OPTIONAL)
  - `no_pseudo_values` - Boolean, disable usage of pseudo values (OPTIONAL)
  - `output_name` - name for the output files (OPTIONAL)
  - `pb_log` - Boolean, enable writing of a log file (OPTIONAL)

### Output parameters
  - `balanced_sbml` - SBML file object with balanced content
  - `balanced_sbtab` - SBtab object with balanced content

## Citation and Contact

If you use parameter balancing, please cite http://pubs.acs.org/doi/abs/10.1021/jp108764b for details.

If you are encountering trouble with any of the above, please file a bug report in GitLab. You can also feel free to file feature requests in the same manner.
