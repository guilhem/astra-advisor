import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


PLUGIN = Path(__file__).resolve().parents[1]
HOOK = json.loads((PLUGIN / 'hooks/hooks.json').read_text())['hooks']['SessionStart'][0]['hooks'][0]


class InstallRoutingProfilesTests(unittest.TestCase):
    def test_hook_installs_missing_profiles_and_preserves_existing_files(self):
        with tempfile.TemporaryDirectory(prefix='astra profiles ') as temporary:
            home = Path(temporary)
            # Run the packaged hook from an unrelated working directory.
            env = {**os.environ, 'CODEX_HOME': str(home), 'PLUGIN_ROOT': str(PLUGIN)}
            command = HOOK['commandWindows' if os.name == 'nt' else 'command']
            command = command.replace('${PLUGIN_ROOT}', str(PLUGIN))
            catalog = home / 'subagent-router'

            def run_hook():
                result = subprocess.run(command, shell=True, cwd=home, env=env,
                                        capture_output=True, text=True, timeout=10)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, '')

            run_hook()
            sources = list((PLUGIN / 'routing').glob('astra-*.json'))
            self.assertEqual(len(sources), 3)
            for source in sources:
                self.assertEqual((catalog / source.name).read_bytes(), source.read_bytes())

            customized = catalog / 'astra-routine.json'
            customized.write_text('{"model": "my-custom-model"}')
            other = catalog / 'other-plugin.json'
            other.write_text('{"model": "another-plugin-model"}')
            before = {p.name: p.read_bytes() for p in catalog.iterdir()}
            missing = catalog / 'astra-complex.json'
            missing.unlink()
            run_hook()
            run_hook()
            self.assertEqual({p.name: p.read_bytes() for p in catalog.iterdir()}, before)


if __name__ == '__main__':
    unittest.main()
