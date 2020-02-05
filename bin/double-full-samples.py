#! /usr/bin/env python

import sys
import os
import glob
import re


def duplicate_samples(in_stream, out_stream):
    ntax_line_pattern = re.compile(
            r'(?P<before>.*dimensions\s+ntax=)(?P<ntax>\d+)(?P<after>\s+nchar=\d+.*;.*)',
            re.IGNORECASE)
    sample_id_line_pattern = re.compile(
            r'(?P<before>.*)(?P<label>\w{4}_\w+_[01])(?P<after>.*)')
    number_of_ntax_lines = 0
    for line in in_stream:
        m = sample_id_line_pattern.match(line)
        if m:
            assert len(sample_id_line_pattern.findall(line)) == 1
            sample_id = m.group('label')
            for l in ('a', 'b'):
                new_label = sample_id + l
                out_line = "{0}{1}{2}\n".format(
                        m.group('before'),
                        new_label,
                        m.group('after'))
                out_stream.write(out_line)
            continue
        m = ntax_line_pattern.match(line)
        if m:
            assert number_of_ntax_lines < 1
            number_of_ntax_lines += 1
            nsamples = int(m.group('ntax'))
            out_line = "{0}{1}{2}\n".format(
                    m.group('before'),
                    nsamples * 2,
                    m.group('after'))
            out_stream.write(out_line)
            continue
        out_stream.write(line)
    assert number_of_ntax_lines == 1

def main_cli(argv = sys.argv):
    for align_path in glob.glob("../alignments/???_full_?????.nex"):
        prefix, extension = os.path.splitext(align_path)
        out_path = prefix + "_doubled" + extension
        with open(align_path, 'r') as in_stream:
            with open (out_path, 'w') as out_stream:
                duplicate_samples(in_stream, out_stream)
    

if __name__ == "__main__":
    main_cli()
