{
  inputs = {
    nixpkgs.url = "github:cachix/devenv-nixpkgs/rolling";
    systems.url = "github:nix-systems/default";
    devenv.url = "github:cachix/devenv";
    nixpkgs-python.url = "github:cachix/nixpkgs-python";
  };

  nixConfig = {
    extra-trusted-public-keys = [
      "devenv.cachix.org-1:w1cLUi8dv3hnoSPGAuibQv+f9TZLr6cv/Hm9XgU50cw="
      "nixpkgs-python.cachix.org-1:hxjI7pFxTyuTHn2NkvWCrAUcNZLNS3ZAvfYNuYifcEU="
    ];
    extra-substituters = [
      "https://devenv.cachix.org"
      "https://nixpkgs-python.cachix.org"
    ];
  };

  outputs = {
    self,
    nixpkgs,
    devenv,
    systems,
    ...
  } @ inputs: let
    forEachSystem = nixpkgs.lib.genAttrs (import systems);
  in {
    packages = forEachSystem (system: {
      devenv-up = self.devShells.${system}.default.config.procfileScript;
      devenv-test = self.devShells.${system}.default.config.test;
    });

    devShells =
      forEachSystem
      (system: let
        pkgs = nixpkgs.legacyPackages.${system};
      in {
        default = devenv.lib.mkShell {
          inherit inputs pkgs;
          modules = [
            {
              packages = with pkgs; [
                git # duh
              ];

              languages = {
                python = {
                  enable = true;
                  version = "3.13";
                  poetry = {
                    enable = true;
                    activate.enable = true;
                    install.enable = true;
                  };
                };

                java = {
                  enable = true;
                };
              };

              enterShell =
                # bash
                ''
                  tput setaf 2; tput bold; echo "git version"; tput sgr0
                  git --version
                  tput setaf 2; tput bold; echo "python version"; tput sgr0
                  python --version
                  tput setaf 2; tput bold; echo "java version"; tput sgr0
                  java --version
                '';

              pre-commit.hooks = {
                autoflake.enable = true;
                ruff.enable = true;
              };
            }
          ];
        };
      });
  };
}
