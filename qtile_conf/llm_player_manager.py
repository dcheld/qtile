import subprocess

from .cache_manager import get_setting, set_setting


class LLMPlayerManager:
    LLM_PLAYER_KEY = "llm_player"
    LLM_OPTIONS = {"Gemini": "gemini", "ChatGPT": "chatgpt", "Claude": "claude"}

    @staticmethod
    def _run_llm_rofi():
        command = """
        source "$HOME/.config/rofi/applets/shared/theme.bash"
        theme="$type/$style"
        printf '%s\n' ChatGPT Claude Gemini | \
            rofi \
                -theme-str "listview {columns: 1; lines: 3;}" \
                -theme-str 'textbox-prompt-colon {str: "🤖";}' \
                -dmenu \
                -i \
                -no-click-to-exit \
                -p "LLM player" \
                -markup-rows \
                -theme "$theme"
        """

        result = subprocess.run(
            ["bash", "-lc", command],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            return None

        selected = result.stdout.strip()
        if not selected:
            return None

        return selected

    @staticmethod
    def _toggle_llm_dropdown(qtile, target):
        sp = qtile.groups_map.get("SPD")
        if sp is None:
            return

        sp.dropdown_toggle(target)

    @staticmethod
    def _kill_current_player(current):
        subprocess.run(
            ["bash", "-lc", f"kill $(xprop -name {current} _NET_WM_PID | awk '{{print $NF}}')"],
            capture_output=True,
            text=True,
        )

    def change_player(self, qtile):
        selected = self._run_llm_rofi()
        if selected is None:
            return

        current = get_setting(self.LLM_PLAYER_KEY)
        target = self.LLM_OPTIONS.get(selected)

        if target is None:
            return

        if current == selected:
            self._toggle_llm_dropdown(qtile, target)
            return

        set_setting(self.LLM_PLAYER_KEY, selected)
        sp = qtile.groups_map.get("SPD")
        if sp is None:
            return

        if current is not None:
            self._kill_current_player(current)

        sp.dropdown_toggle(target)

    def toggle_player(self, qtile):
        selected = get_setting(self.LLM_PLAYER_KEY)
        if selected is None:
            qtile.spawn("notify-send 'LLM' 'Nenhum player salvo ainda' -u normal")
            return

        target = self.LLM_OPTIONS.get(selected)
        if target is None:
            return

        self._toggle_llm_dropdown(qtile, target)


llm_player_manager = LLMPlayerManager()
