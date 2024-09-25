if not contains "$HOME/.grit/bin" $PATH
    # Prepending path in case a system-installed binary needs to be overridden
    set -x PATH "$HOME/.grit/bin" $PATH
end
