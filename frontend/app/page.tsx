export default async function Home() {
  let status = "unknown"
  try {
    const r = await fetch(process.env.NEXT_PUBLIC_API_URL + "/health",
      { cache: "no-store" })
    status = (await r.json()).status
  } catch { status = "unreachable" }
  return (
    <main className="p-8 font-mono">
      <h1 className="text-2xl font-medium mb-2">SpatialPhysics AI</h1>
      <p className="text-sm text-gray-400 mb-8">Phase 1 — Cloud Skeleton</p>
      <div className="border rounded-lg p-4 max-w-xs">
        <p className="text-xs text-gray-400 mb-1">API status</p>
        <p className={status==="ok"?"text-green-600":"text-red-500"}>
          {status}
        </p>
      </div>
    </main>
  )
}