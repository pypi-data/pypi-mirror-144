{
    'derived_from' : 'jwst_nirspec_regions_0002.rmap',
    'extra_keys' : ('META.EXPOSURE.TYPE',),
    'file_ext' : '.json',
    'filekind' : 'REGIONS',
    'filetype' : 'REGIONS',
    'instrument' : 'NIRSPEC',
    'mapping' : 'REFERENCE',
    'name' : 'jwst_nirspec_regions_0003.rmap',
    'observatory' : 'JWST',
    'parkey' : (('META.INSTRUMENT.DETECTOR', 'META.INSTRUMENT.GRATING', 'META.INSTRUMENT.FILTER', 'META.EXPOSURE.TYPE'),),
    'reference_to_dataset' : {'EXP_TYPE': 'META.EXPOSURE.TYPE', 'FILTER': 'META.INSTRUMENT.FILTER', 'DETECTOR': 'META.INSTRUMENT.DETECTOR', 'GRATING': 'META.INSTRUMENT.GRATING'},
    'rmap_relevance' : '(META.EXPOSURE.TYPE not in ("MIR_IMAGE", "NRC_IMAGE", "NIS_IMAGE", "MIR_LRS-FIXEDSLIT", "MIR_LRS-SLITLESS"))',
    'sha1sum' : '49857936deae765788cad0f839e2ed4206e539e0',
    'suffix' : 'regions',
    'text_descr' : 'Regions',
}
