import libadalang as lal

# The list of types to generate Write procedures:
types_to_print = {
    #  'Message',
    'RequestMessage',
    #  'ResponseMessage',
    'NotificationMessage',
    'CancelParams',
    'Position',
    'Span',
    'CodeActionKind',
    'AlsReferenceKind',
    #  'AlsReferenceKind_Array',
    #  'AlsReferenceKind_Set',
    'Location',
    'LocationLink',
    #  'Location_Or_Link_Kind',
    #  'Location_Or_Link_Vector',
    'DiagnosticSeverity',
    'DiagnosticTag',
    'DiagnosticRelatedInformation',
    'Diagnostic',
    #  'Command',
    'TextEdit',
    'TextDocumentIdentifier',
    #  'VersionedTextDocumentIdentifier',
    'TextDocumentEdit',
    #  'CreateFileOptions',
    #  'CreateFile',
    #  'RenameFileOptions',
    #  'RenameFile',
    #  'DeleteFileOptions',
    #  'DeleteFile',
    #  'Document_Change_Kind',
    #  'Document_Change',
    #  'WorkspaceEdit',
    'TextDocumentItem',
    'TextDocumentPositionParams',
    #  'DocumentFilter',
    #  'DocumentSelector',
    'dynamicRegistration',
    'ResourceOperationKind',
    'FailureHandlingKind',
    'WorkspaceEditClientCapabilities',
    'SymbolKind',
    'symbolKindCapabilities',
    'Als_Visibility',
    'WorkspaceSymbolClientCapabilities',
    'WorkspaceClientCapabilities',
    'MarkupKind',
    'MarkupContent',
    #  'String_Or_MarkupContent',
    'SaveOptions',
    'TextDocumentSyncClientCapabilities',
    'CompletionItemTag',
    'CompletionItemTagSupport',
    'completionItemCapability',
    'CompletionItemKind',
    'CompletionItemKindSetCapabilities',
    'CompletionClientCapabilities',
    'HoverClientCapabilities',
    'parameterInformation_Capability',
    'signatureInformation_Capability',
    'SignatureHelpClientCapabilities',
    'DocumentSymbolClientCapabilities',
    'DeclarationClientCapabilities',
    'codeActionKindCapability',
    'codeActionLiteralSupport_Capability',
    'CodeActionClientCapabilities',
    'DocumentLinkClientCapabilities',
    'RenameClientCapabilities',
    'DiagnosticTagSupport',
    'PublishDiagnosticsClientCapabilities',
    'FoldingRangeClientCapabilities',
    'TextDocumentClientCapabilities',
    'WindowClientCapabilities',
    'ClientCapabilities',
    'WorkspaceFolder',
    #  'ProgressParam',
    'WorkDoneProgressCreateParams',
    #  'WorkDoneProgressParams',
    #  'PartialResultParams',
    #  'Progress_Partial_Params',
    #  'Text_Progress_Partial_Params',
    #  'Text_Progress_Params',
    'ProgramInfo',
    'Trace_Kind',
    #  'InitializeParams',
    #  'WorkDoneProgressOptions',
    'TextDocumentSyncKind',
    'TextDocumentSyncOptions',
    #  'Optional_TextDocumentSyncOptions',
    'CompletionOptions',
    'SignatureHelpOptions',
    #  'TextDocumentRegistrationOptions',
    'TSW_RegistrationOptions',
    #  'Provider_Options',
    'CodeActionOptions',
    'CodeLensOptions',
    'DocumentOnTypeFormattingOptions',
    'RenameOptions',
    'DocumentLinkOptions',
    'ExecuteCommandOptions',
    'WorkspaceFoldersServerCapabilities',
    'workspace_Options',
    'ServerCapabilities',
    'InitializeResult',
    'InitializedParams',
    #  'InitializeError',
    'MessageType',
    'ShowMessageParams',
    'ShowMessageRequestParams',
    'LogMessageParams',
    #  'TextDocumentChangeRegistrationOptions',
    #  'TextDocumentSaveRegistrationOptions',
    #  'CompletionRegistrationOptions',
    #  'SignatureHelpRegistrationOptions',
    #  'CodeLensRegistrationOptions',
    #  'DocumentLinkRegistrationOptions',
    #  'DocumentOnTypeFormattingRegistrationOptions',
    #  'ExecuteCommandRegistrationOptions',
    #  'Registration_Option',
    #  'Registration',
    #  'Registration_Array',
    #  'RegistrationParams',
    #  'Unregistration',
    'DidChangeConfigurationParams',
    'DidOpenTextDocumentParams',
    'TextDocumentContentChangeEvent',
    'DidChangeTextDocumentParams',
    'TextDocumentSaveReason',
    #  'WillSaveTextDocumentParams',
    'DidSaveTextDocumentParams',
    'DidCloseTextDocumentParams',
    'FileChangeType',
    #  'FileEvent',
    #  'DidChangeWatchedFilesParams',
    'PublishDiagnosticsParams',
    'InsertTextFormat',
    'CompletionItem',
    'CompletionList',
    #  'MarkedString',
    #  'MarkupContent_Or_MarkedString_Vector',
    'Hover',
    #  'Parameter_Label',
    'ParameterInformation',
    'SignatureInformation',
    'SignatureHelp',
    'ReferenceContext',
    'ReferenceParams',
    'DocumentHighlightKind',
    'DocumentHighlight',
    'DocumentSymbolParams',
    #  'DocumentSymbol',
    #  'DocumentSymbol_Tree',
    'SymbolInformation',
    #  'Symbol_Vector',
    'WorkspaceSymbolParams',
    'CodeActionContext',
    'CodeActionParams',
    #  'CodeLensParams',
    #  'CodeLens',
    #  'DocumentLinkParams',
    #  'DocumentLink',
    'FormattingOptions',
    'DocumentFormattingParams',
    'DocumentRangeFormattingParams',
    'DocumentOnTypeFormattingParams',
    'RenameParams',
    #  'ExecuteCommandParams',
    'ApplyWorkspaceEditParams',
    'ApplyWorkspaceEditResult',
    'WorkDoneProgressBegin',
    'WorkDoneProgressReport',
    'WorkDoneProgressEnd',
    #  'Progress_Kind',
    #  'Progress_Params',
    'WorkspaceFoldersChangeEvent',
    'DidChangeWorkspaceFoldersParams',
    'ConfigurationItem',
    'ConfigurationParams',
    #  'WatchKind',
    #  'WatchKind_Set',
    'FileSystemWatcher',
    'DidChangeWatchedFilesRegistrationOptions',
    'CompletionTriggerKind',
    'CompletionContext',
    'CompletionParams',
    #  'CodeAction',
    #  'CodeActionRegistrationOptions',
    'RGBA_Color',
    'ColorInformation',
    'ColorPresentationParams',
    'ColorPresentation',
    #  'RenameRegistrationOptions',
    'FoldingRangeParams',
    'FoldingRange',
    'DocumentColorParams',
    #  'HoverParams',
    #  'SignatureHelpParams',
    #  'DeclarationParams',
    #  'DefinitionParams',
    #  'TypeDefinitionParams',
    #  'ImplementationParams',
    #  'DocumentHighlightParams',
    'SelectionRangeParams',
    'SelectionRange',
    'ALS_Subprogram_And_References',
    #  'ALS_Debug_Kinds',
    #  'ALSDebugParams',
    }

spec_header = """--  Automatically generated, do not edit.
with Ada.Streams;
with LSP.Messages;

package LSP.Message_IO is
"""

body_header = """--  Automatically generated, do not edit.
with GNATCOLL.JSON;

with LSP.JSON_Streams;
with LSP.Messages;                 use LSP.Messages;
with LSP.Types;                    use LSP.Types;

package body LSP.Message_IO is
   pragma Style_Checks ("M175");
"""

file_footer = """
end LSP.Message_IO;
"""

io_spec = """
   procedure {kind}_{type}
     (S : access Ada.Streams.Root_Stream_Type'Class;
      V : {out}LSP.Messages.{type});
"""

io_header = """
   procedure {kind}_{type}
     (S : access Ada.Streams.Root_Stream_Type'Class;
      V : {out}{type})
   is
{unref}      JS : LSP.JSON_Streams.JSON_Stream'Class renames
        LSP.JSON_Streams.JSON_Stream'Class (S.all);
"""

io_footer = """\
   end {kind}_{type};
"""

write_component = \
    {
     "LSP_String": """\
      JS.Key ("{key}");
      LSP.Types.{kind} (S, V.{name});
""",
     "DocumentUri": """\
      JS.Key ("{key}");
      LSP.Types.{kind} (S, V.{name});
""",
     "Boolean": """\
      {kind}_Boolean (JS, +"{key}", V.{name});
""",
     "": """\
      JS.Key ("{key}");
      {type}'{kind} (S, V.{name});
"""
    }

io_pos_enum = {
    'Read': """\
      V := {type}'Val (JS.Read.Get - {offset});
""",
    'Write': """\
      JS.Write
        (GNATCOLL.JSON.Create
           (Integer'({type}'Pos (V)) + {offset}));
"""
}

io_string_enum_header = {
    'Read': """
      Text : constant Standard.String := JS.Read.Get;
   begin
      """,
    'Write': """
      function To_String
        (Value : {type})
         return GNATCOLL.JSON.UTF8_String;

      function To_String
        (Value : {type})
         return GNATCOLL.JSON.UTF8_String is
      begin
         case Value is
"""
}

io_string_enum_case = {
    'Read': """if Text = "{key}" then
         V := {name};
      els""",
    'Write': """\
            when {name} =>
               return "{key}";
"""
}

io_string_enum_footer = {
    'Read': """e
         V := {type}'First;
      end if;
""",
    'Write': """\
         end case;
      end To_String;

   begin
      JS.Write (GNATCOLL.JSON.Create (To_String (V)));
"""
}

# The list of enumeration type represented as strings
enum_as_string = [
    'AlsReferenceKind',
    'CodeActionKind',
    'ResourceOperationKind',
    'FailureHandlingKind',
    'MarkupKind',
    'Trace_Kind']

# The map to substitute words reserved in Ada:
reserver_named = \
   {
    "abortapplying": "abort",
    "first": "start",
    "last": "end",
    "loc": "location",    # for ALS_Subprogram_And_References
    "span": "range",
    "the_type": "type",
    "simple": "reference",  # For AlsReferenceKind
    "write": "write",
    "static_call": "call",
    "dispatching_call": "dispatching call",
    "parent": "parent",
    "child": "child",
    "empty": "",            # For CodeActionKind
    "quickfix": "quickfix",
    "refactor": "refactor",
    "refactorextract": "refactor.extract",
    "refactorinline": "refactor.inline",
    "refactorrewrite": "refactor.rewrite",
    "source": "source",
    "sourceorganizeimports": "source.organizeImports",
    "messages": "messages_trace",  # for Trace_Kind
    }


def get_key(field):
    lower = field.lower()
    if lower in reserver_named:
        return reserver_named[lower]
    else:
        return field


def write_format(type):
    if type in write_component:
        return write_component[type]
    else:
        return write_component[""]


def filter(x):
    return isinstance(x, lal.TypeDecl) \
        and not isinstance(x, lal.AnonymousTypeDecl) \
        and x.p_defining_name.token_start.text in types_to_print


def print_spec(file, node):
    name = node.p_defining_name.token_start.text
    print name
    file.write(io_spec.format(type=name, kind='Read', out='out '))
    file.write(io_spec.format(type=name, kind='Write', out=''))


def get_components(node):
    if isinstance(node, lal.DerivedTypeDef):
        parent = node.f_subtype_indication.p_designated_type_decl
        result = get_components(parent.f_type_def)
    else:
        result = []

    result += list(node.finditer(lal.ComponentDecl))

    return result


def print_components(file, kind, node):
    file.write('   begin\n')
    file.write('      JS.Start_Object;\n')

    for x in get_components(node):
        name = x.p_defining_name.token_start.text
        tp = x.f_component_def.f_type_expr.f_name.full_name
        txt = write_format(tp).format(key=get_key(name),
                                      kind=kind,
                                      name=name,
                                      type=tp)
        file.write(txt)

    file.write('      JS.End_Object;\n')


def print_enums(file, kind, type, node):
    if type not in enum_as_string:
        offset = 0 if type == 'TextDocumentSyncKind' else 1
        file.write('   begin\n')
        txt = io_pos_enum[kind].format(type=type, offset=offset)
    else:
        txt = io_string_enum_header[kind].format(type=type)
        for x in node.finditer(lal.EnumLiteralDecl):
            name = x.p_defining_name.token_start.text
            txt += io_string_enum_case[kind].format(name=name,
                                                    key=get_key(name))
        txt += io_string_enum_footer[kind].format(type=type)

    file.write(txt)


def print_body(file, node):
    name = node.p_defining_name.token_start.text

    unref = '      pragma Unreferenced (V);\n\n' if \
        len(list(node.finditer(lal.NullRecordDef))) else ''

    def print_decls_and_statements(kind):
        file.write(io_header.format(type=name,
                                    kind=kind,
                                    out='' if kind == 'Write' else 'out ',
                                    unref=unref))
        if isinstance(node.f_type_def, lal.EnumTypeDef):
            print_enums(file, kind, name, node.f_type_def)
        else:
            print_components(file, kind, node.f_type_def)

        file.write(io_footer.format(type=node.p_defining_name.token_start.text,
                                    kind=kind))
    print_decls_and_statements('Read')
    print_decls_and_statements('Write')


def print_io():
    up = lal.UnitProvider.for_project("gnat/lsp.gpr")
    ctx = lal.AnalysisContext(unit_provider=up)
    unit = ctx.get_from_file("source/protocol/lsp-messages.ads")
    ads = open("source/protocol/generated/lsp-message_io.ads", 'wb')
    ads.write(spec_header)
    adb = open("source/protocol/generated/lsp-message_io.adb", 'wb')
    adb.write(body_header)

    for x in unit.root.finditer(filter):
        print_spec(ads, x)
        print_body(adb, x)

    ads.write(file_footer)
    adb.write(file_footer)

if __name__ == '__main__':
    print_io()
