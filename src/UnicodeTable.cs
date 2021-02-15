using System.Runtime.InteropServices;

namespace Unidecode.NET
{
  public static class UnicodeTable
  {
    public static string Lookup(int high, int low)
    {
      var result = UnicodeDll.Lookup(high, low);

      return Marshal.PtrToStringAnsi(result);
    }
  }
}
