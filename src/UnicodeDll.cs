using System;
using System.Runtime.InteropServices;

namespace Unidecode.NET
{
  public static class UnicodeDll
  {
    [DllImport("unidecode_native", CallingConvention = CallingConvention.Cdecl)]
    public static extern IntPtr Lookup(int high, int low);
  }
}
