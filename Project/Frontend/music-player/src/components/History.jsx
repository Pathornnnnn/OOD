export default function History({ history }) {
  return (
    <div className="mt-4 bg-gray-100 p-3 rounded">
      <h4 className="font-semibold mb-2">History</h4>
      <ul className="space-y-1 text-gray-700">
        {history.map((song, index) => (
          <li key={index}>{song.title}</li>
        ))}
      </ul>
    </div>
  );
}
