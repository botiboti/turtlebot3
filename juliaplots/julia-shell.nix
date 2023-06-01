{ pkgs ? import <nixpkgs> { } }:

with pkgs;
let
  julia = julia-bin;
  d = version: "v${lib.concatStringsSep "." (lib.take 2 (lib.splitString "." version))}";
  extraLibs = [
    ffmpeg
    # ImageMagick.jl ==========================
    # imagemagickBig
    # HDF5.jl =================================
    # hdf5
    # Cairo.jl ================================
    # cairo gettext pango.out glib.out
    # Gtk.jl ==================================
    # gtk3 gdk_pixbuf
    # GZip.jl required by DataFrames.jl =======
    # gzip zlib
    # GR.jl which runs without Xrender & Xext =
    # but cannot save files ===================
    # org.libXt xorg.libX11 xorg.libXrender xorg.libXext glfw freetype
    # Flux.jl =================================
    # cudatoolkit linuxPackages.nvidia_x11 git gitRepo gnupg autoconf curl
    # procps gnumake utillinux m4 gperf unzip libGLU_combined ncurses5 stdenv.cc binutils
    # xorg.libXi xorg.libXmu freeglut xorg.libXext xorg.libX11 xorg.libXv xorg.libXrandr zlib
    # Arpack.jl ===============================
    # arpack gfortran.cc
    (pkgs.runCommand "openblas64_" { } ''
      mkdir -p "$out"/lib/
      ln -s ${openblasCompat}/lib/libopenblas.so "$out"/lib/libopenblas64_.so.0
    '')
  ];
in
stdenv.mkDerivation rec {
  name = "julia-env";
  version = julia.version;
  nativeBuildInputs = [ makeWrapper cacert git pkgconfig which ];
  buildInputs = [
    julia
    /* jupyterEnv  # my custom jupyter */
  ] ++ extraLibs;
  phases = [ "installPhase" ];
  installPhase = ''
    export LD_LIBRARY_PATH=${lib.makeLibraryPath extraLibs}
    # pushd $JULIA_PKGDIR/${d version}
    makeWrapper ${julia}/bin/julia $out/bin/julia \
        --prefix LD_LIBRARY_PATH : "$LD_LIBRARY_PATH" \
        --set JULIA_PKGDIR $JULIA_PKGDIR
  '';
}
